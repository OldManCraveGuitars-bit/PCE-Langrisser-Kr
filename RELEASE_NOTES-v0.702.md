![PCE 랑그릿사 한국어판 메인 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/title.png)

# PCE-Langrisser-Kr v0.702 — 단일 BIN 실기 진단판

**수정 완료판이 아닙니다.** [실기 이슈 2](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/2)에서 v0.701도 RUN 이후 글자 깨짐과 1화 진입 전 리셋이 동일하게 재현됐습니다. v0.702는 Turbo EverDrive Pro가 별도 파일의 39번 트랙을 읽는 과정이 원인인지 구분하기 위한 프리릴리스입니다. 실기 결과는 아직 없습니다.

## v0.701 대비 변경

- 기존 본편 BIN과 `MODE1/2352` 39번 트랙을 **한 BIN 파일**로 합쳤습니다.
  CUE는 39개 트랙을 유지하지만 `FILE` 항목이 하나입니다.
- 게임 본문과 39번 트랙의 바이트는 v0.701과 동일합니다. 번역·그림·게임 코드의 수정판이 아닙니다.
- 수동 BPS ZIP과 Windows 패처 EXE를 함께 제공합니다. 둘 다 일본판 원본 ISO에 적용하며, 결과는 BIN 하나와 CUE 하나입니다. 기존 버전의 파일과 섞지 마세요.

## 검증 범위

- 지원 일본판 원본 SHA-256: `ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`.
- 결과 단일 BIN SHA-256: `069EAC1E5F761C53647F94BD96C0D66CA58FD2799F014A933E3E90FF74054E4D` (559,105,680바이트).
- BPS를 원본에 재적용한 결과가 기대 BIN과 정확히 일치했습니다.
- 같은 에뮬레이터 입력으로 60,000회 갱신을 실행했습니다. v0.701과 RAM·VRAM 6표본, CD 읽기·실행 기록이 일치했습니다. 실기 검증이나 전체 플레이 완료를 뜻하지 않습니다.
- **Turbo EverDrive Pro 및 기타 실기에서 정상 동작하는지는 미확인입니다.** RUN 직후 첫 메뉴 글자, 1화 설명, 맵 진입, BIOS 복귀 여부를 [이슈 2](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/2)에 제보해 주세요.

본인 소유의 지원 일본판 ISO를 선택해 패치한 다음 결과 **CUE**를 실행하세요. 원본 게임 이미지와 BIOS는 포함하지 않습니다. 이전 세이브스테이트를 불러오지 말고 새로 부팅하세요. 기존 검수 한계는 [v0.7 릴리스 노트](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/blob/main/RELEASE_NOTES-v0.7.md)를 참고하세요.
