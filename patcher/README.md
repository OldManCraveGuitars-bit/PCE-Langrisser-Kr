# Windows 원클릭 진단 패처 v0.705

**게임용 패치가 아닙니다. 실기 읽기 오류를 좁히기 위한 진단 화면만 실행합니다.**
기존 한국어판과 저장 파일을 교체하지 말고 별도 폴더에서 시험하세요.

`PCE-Langrisser-Kr-v0.705-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
원본 게임과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 빈 결과 폴더를 지정하고 `진단 이미지 만들기`를 누릅니다.
3. 생성된 BIN과 CUE를 함께 복사하고 실기에서 CUE를 엽니다.
4. BIOS에서 RUN을 누른 뒤 `DONE - PHOTO THIS SCREEN`이 나오면 화면 전체를 촬영해 주세요.
   중간에 멈추면 그 화면을 보내 주세요.

내부 파일명 `ADPCM_DIAGNOSTIC_V374.bin/.cue`는 정상입니다.
원래 38트랙 구성을 유지하며, 이전 세이브스테이트를 불러오면 안 됩니다.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며, 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

진단 결과 BIN SHA-256:

```text
E652F5D01686A09FF1C5881D8782BFEFAD89DB7D569ED9D86137CE57F74EF65E
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
릴리스 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.705-patch -OutputDirectory C:/path/to/output
```

v0.704까지 실기에서 같은 증상이 보고됐습니다. v0.705의 실기 결과는 아직 없습니다.
에뮬레이터에서 여섯 검사가 통과했고, 의도적으로 틀린 데이터도 검출했지만
실제 게임 상태·인터럽트 경쟁·전체 캠페인을 검증한 것은 아닙니다.
