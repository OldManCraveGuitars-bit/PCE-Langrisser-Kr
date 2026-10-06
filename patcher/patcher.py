"""Offline, ROM-free Windows installer for the v0.702 BPS patch.

The bundled assets are only a BPS delta and single-BIN CUE sheet.
The user supplies the supported Japanese raw ISO; no game or BIOS is bundled.
"""

from __future__ import annotations

import argparse
import hashlib
import mmap
import os
from pathlib import Path
import queue
import struct
import sys
import threading
import time
import zlib


SOURCE_SIZE = 559_051_584
SOURCE_SHA256 = "ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68"
TARGET_SIZE = 559_105_680
TARGET_SHA256 = "069EAC1E5F761C53647F94BD96C0D66CA58FD2799F014A933E3E90FF74054E4D"
BIN_NAME = "LANGRISSER_KR_SINGLE_BIN_TRACK39_DIAG_V371.bin"
CUE_NAME = "LANGRISSER_KR_SINGLE_BIN_TRACK39_DIAG_V371.cue"
PATCH_NAME = "PCE-Langrisser-Kr-v0.702-patch.bps"
ASSET_HASHES = {
    PATCH_NAME: "EB5AE1D1FC43505FE6B6E10A6FD5C0E8889466DAD8160B77E4CB1BAFDF02FB16",
    CUE_NAME: "08C114333AAB0F7B5480A031C24335B171BEB9A16D197A24BB4756BBEC866535",
}
CHUNK = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def source_checksums(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    crc = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK), b""):
            digest.update(chunk)
            crc = zlib.crc32(chunk, crc)
    return digest.hexdigest().upper(), crc


def varint(data: bytes, cursor: int, end: int) -> tuple[int, int]:
    value = 0
    scale = 1
    while cursor < end:
        octet = data[cursor]
        cursor += 1
        value += (octet & 0x7F) * scale
        if octet & 0x80:
            return value, cursor
        scale <<= 7
        value += scale
        if scale > 1 << 63:
            break
    raise ValueError("손상된 BPS 가변 정수입니다.")


def signed_offset(value: int) -> int:
    return -(value >> 1) if value & 1 else value >> 1


def parse_patch_header(patch: bytes) -> tuple[int, int, int, int, int, int]:
    if len(patch) < 16 or patch[:4] != b"BPS1":
        raise ValueError("BPS 패치 형식이 아닙니다.")
    end = len(patch) - 12
    if zlib.crc32(patch[:-4]) != struct.unpack_from("<I", patch, end + 8)[0]:
        raise ValueError("BPS 패치 자체의 CRC가 맞지 않습니다.")
    cursor = 4
    source_size, cursor = varint(patch, cursor, end)
    target_size, cursor = varint(patch, cursor, end)
    metadata_size, cursor = varint(patch, cursor, end)
    cursor += metadata_size
    if cursor > end or source_size != SOURCE_SIZE or target_size != TARGET_SIZE:
        raise ValueError("지원하지 않는 패치 크기 또는 손상된 메타데이터입니다.")
    source_crc, target_crc = struct.unpack_from("<II", patch, end)
    return cursor, end, source_crc, target_crc, source_size, target_size


def apply_bps(patch: bytes, source: Path, output: Path,
              progress=lambda _message: None) -> None:
    cursor, end, source_crc, target_crc, source_size, target_size = parse_patch_header(patch)
    if source.stat().st_size != source_size:
        raise ValueError("지원 원본 ISO의 크기가 다릅니다.")
    progress("원본 ISO 해시 확인 중…")
    source_sha, actual_crc = source_checksums(source)
    if source_sha != SOURCE_SHA256 or actual_crc != source_crc:
        raise ValueError("지원하는 일본 원본 ISO가 아닙니다. 원본 파일은 수정하지 않았습니다.")

    progress("BPS 패치 적용 중…")
    last_report = 0.0
    with source.open("rb") as src_file, output.open("x+b") as dst_file:
        dst_file.truncate(target_size)
        with mmap.mmap(src_file.fileno(), 0, access=mmap.ACCESS_READ) as src, \
                mmap.mmap(dst_file.fileno(), 0, access=mmap.ACCESS_WRITE) as dst:
            written = 0
            source_relative = 0
            target_relative = 0
            while written < target_size:
                command, cursor = varint(patch, cursor, end)
                mode = command & 3
                length = (command >> 2) + 1
                if length > target_size - written:
                    raise ValueError("BPS 출력 경계를 벗어났습니다.")

                if mode == 0:  # SourceRead, same offset as output
                    if written + length > source_size:
                        raise ValueError("BPS 원본 읽기 경계를 벗어났습니다.")
                    for offset in range(0, length, CHUNK):
                        n = min(CHUNK, length - offset)
                        dst[written + offset:written + offset + n] = src[written + offset:written + offset + n]
                elif mode == 1:  # TargetRead, literal bytes from patch
                    if cursor + length > end:
                        raise ValueError("BPS 리터럴 데이터가 잘렸습니다.")
                    for offset in range(0, length, CHUNK):
                        n = min(CHUNK, length - offset)
                        dst[written + offset:written + offset + n] = patch[cursor + offset:cursor + offset + n]
                    cursor += length
                elif mode == 2:  # SourceCopy
                    delta, cursor = varint(patch, cursor, end)
                    source_relative += signed_offset(delta)
                    if source_relative < 0 or source_relative + length > source_size:
                        raise ValueError("BPS 원본 복사 경계를 벗어났습니다.")
                    for offset in range(0, length, CHUNK):
                        n = min(CHUNK, length - offset)
                        dst[written + offset:written + offset + n] = src[source_relative + offset:source_relative + offset + n]
                    source_relative += length
                else:  # TargetCopy, may intentionally overlap its own output
                    delta, cursor = varint(patch, cursor, end)
                    target_relative += signed_offset(delta)
                    if target_relative < 0 or target_relative >= written:
                        raise ValueError("BPS 출력 복사 위치가 잘못되었습니다.")
                    copied = 0
                    while copied < length:
                        destination = written + copied
                        origin = target_relative + copied
                        gap = destination - origin
                        n = min(CHUNK, length - copied)
                        if gap >= n:
                            dst[destination:destination + n] = dst[origin:origin + n]
                        else:
                            pattern = dst[origin:destination]
                            dst[destination:destination + n] = (pattern * ((n + gap - 1) // gap))[:n]
                        copied += n
                    target_relative += length
                written += length
                now = time.monotonic()
                if now - last_report >= 0.3:
                    progress(f"BPS 패치 적용 중… {written * 100 // target_size}%")
                    last_report = now
            if cursor != end:
                raise ValueError("BPS 명령 끝 위치가 맞지 않습니다.")
            dst.flush()

    progress("결과 BIN 해시 확인 중…")
    actual_sha, actual_crc = source_checksums(output)
    if actual_sha != TARGET_SHA256 or actual_crc != target_crc:
        raise ValueError("패치 결과 검증 실패: 출력 BIN을 배포하지 않습니다.")


def install(source: Path, destination: Path, assets: Path,
            progress=lambda _message: None) -> Path:
    source = source.resolve(strict=True)
    if not source.is_file():
        raise ValueError("원본 ISO 파일을 선택하세요.")
    asset_paths = {name: assets / name for name in ASSET_HASHES}
    for name, path in asset_paths.items():
        if not path.is_file() or sha256_file(path) != ASSET_HASHES[name]:
            raise ValueError(f"내장 파일 검증 실패: {name}")
    cue = asset_paths[CUE_NAME].read_text(encoding="ascii")
    if (cue.count("TRACK ") != 39 or cue.count('FILE "') != 1
            or BIN_NAME not in cue or "TRACK 39 MODE1/2352" not in cue):
        raise ValueError("CUE의 트랙 구성이나 파일명이 맞지 않습니다.")
    patch = asset_paths[PATCH_NAME].read_bytes()
    parse_patch_header(patch)

    destination.mkdir(parents=True, exist_ok=True)
    destination = destination.resolve()
    final_paths = [destination / BIN_NAME, destination / CUE_NAME]
    temporary = destination / (BIN_NAME + ".partial")
    if source in final_paths or any(path.exists() for path in [*final_paths, temporary]):
        raise FileExistsError("출력 위치에 같은 이름의 파일이 있습니다. 빈 폴더를 선택하세요.")
    created: list[Path] = []
    try:
        apply_bps(patch, source, temporary, progress)
        created.append(temporary)
        for name, destination_file in ((CUE_NAME, final_paths[1]),):
            with destination_file.open("xb") as target_file:
                created.append(destination_file)
                with asset_paths[name].open("rb") as source_file:
                    for block in iter(lambda: source_file.read(CHUNK), b""):
                        target_file.write(block)
        if sha256_file(final_paths[1]) != ASSET_HASHES[CUE_NAME]:
            raise ValueError("CUE 복사 검증 실패")
        temporary.replace(final_paths[0])
        created.remove(temporary)
        created.append(final_paths[0])
        progress("완료. 에뮬레이터에서 CUE 파일을 여세요.")
        return final_paths[1]
    except Exception:
        # Only files created by this invocation are eligible for removal.
        for path in [temporary, *created]:
            if path.exists():
                path.unlink()
        raise


def asset_directory() -> Path:
    root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return root / "assets"


def gui(assets: Path) -> None:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk

    root = tk.Tk()
    root.title("PCE 랑그릿사 한국어 패치 v0.702 (실기 진단판)")
    root.geometry("650x250")
    root.resizable(False, False)
    frame = ttk.Frame(root, padding=18)
    frame.pack(fill="both", expand=True)
    source_value = tk.StringVar()
    dest_value = tk.StringVar()
    status = tk.StringVar(value="본인 소유의 일본 원본 ISO를 선택하세요. 원본 파일은 변경하지 않습니다.")
    events: queue.Queue[tuple[str, str]] = queue.Queue()

    def select_source():
        selected = filedialog.askopenfilename(title="일본 원본 ISO 선택", filetypes=[("ISO/BIN", "*.iso *.bin"), ("모든 파일", "*.*")])
        if selected:
            source_value.set(selected)
            dest_value.set(str(Path(selected).parent / "PCE-Langrisser-Kr-v0.702"))

    def select_destination():
        selected = filedialog.askdirectory(title="출력 폴더의 상위 폴더 선택")
        if selected:
            dest_value.set(str(Path(selected) / "PCE-Langrisser-Kr-v0.702"))

    ttk.Label(frame, text="일본 원본 ISO").grid(row=0, column=0, sticky="w")
    ttk.Entry(frame, textvariable=source_value, width=68).grid(row=1, column=0, sticky="ew", pady=(2, 12))
    ttk.Button(frame, text="찾기", command=select_source).grid(row=1, column=1, padx=(8, 0), pady=(2, 12))
    ttk.Label(frame, text="결과 폴더 (약 560 MB의 여유 공간 필요)").grid(row=2, column=0, sticky="w")
    ttk.Entry(frame, textvariable=dest_value, width=68).grid(row=3, column=0, sticky="ew", pady=(2, 12))
    ttk.Button(frame, text="변경", command=select_destination).grid(row=3, column=1, padx=(8, 0), pady=(2, 12))
    ttk.Label(frame, textvariable=status, wraplength=600).grid(row=4, column=0, columnspan=2, sticky="w")
    button = ttk.Button(frame, text="검사 후 패치 적용")
    button.grid(row=5, column=0, columnspan=2, pady=(14, 0))

    def launch():
        if not source_value.get() or not dest_value.get():
            messagebox.showerror("파일 선택 필요", "원본 ISO와 결과 폴더를 지정하세요.")
            return
        source = Path(source_value.get())
        destination = Path(dest_value.get())
        button.configure(state="disabled")

        def worker():
            try:
                result = install(source, destination, assets, lambda message: events.put(("status", message)))
                events.put(("done", str(result)))
            except Exception as exc:
                events.put(("error", str(exc)))

        threading.Thread(target=worker, daemon=True).start()

    button.configure(command=launch)

    def poll():
        try:
            while True:
                kind, message = events.get_nowait()
                if kind == "status":
                    status.set(message)
                elif kind == "done":
                    button.configure(state="normal")
                    messagebox.showinfo("패치 완료", f"완료했습니다. 에뮬레이터에서 다음 CUE를 여세요:\n{message}")
                else:
                    button.configure(state="normal")
                    status.set("실패: " + message)
                    messagebox.showerror("패치 실패", message)
        except queue.Empty:
            pass
        root.after(100, poll)

    root.after(100, poll)
    root.mainloop()


def main() -> int:
    parser = argparse.ArgumentParser(description="PCE Langrisser v0.702 ROM-free patcher (single-BIN hardware diagnostic)")
    parser.add_argument("--input", type=Path, help="supported Japanese raw ISO")
    parser.add_argument("--output-dir", type=Path, help="directory for patched single BIN and CUE")
    parser.add_argument("--assets", type=Path, default=asset_directory(), help=argparse.SUPPRESS)
    arguments = parser.parse_args()
    if bool(arguments.input) != bool(arguments.output_dir):
        parser.error("--input and --output-dir must be specified together")
    if not arguments.input:
        gui(arguments.assets)
        return 0
    try:
        result = install(arguments.input, arguments.output_dir, arguments.assets, print)
        print(result)
        return 0
    except Exception as exc:
        print(f"패치 실패: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
