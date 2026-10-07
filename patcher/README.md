# Windows 원클릭 패처 v0.707

**실제 게임 첫 한글 표시 시점에서 검사 화면으로 멈추는 진단 전용판입니다.**
게임 진행용이나 수정 완료판이 아닙니다. 기존 한국어판과 저장 파일은 보존하세요.

`PCE-Langrisser-Kr-v0.707-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
게임 원본과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 별도 결과 폴더를 지정하고 `검사 후 진단 이미지 만들기`를 누릅니다.
3. 생성된 BIN과 CUE를 같은 폴더에 복사한 뒤 CUE로 새로 부팅합니다.
4. 이전 버전 세이브스테이트는 불러오지 마세요.
5. 오프닝을 넘기고 타이틀에서 RUN을 누릅니다. `V378 LIVE GAME FONT CHECK`가
   나오면 완료 또는 멈춘 화면 전체를 촬영하세요. 이후 게임 진행은 안 됩니다.
   기존처럼 깨지거나 BIOS로 돌아가면 그 상황을 알려 주세요.

내부 파일명 `LANGRISSER_LIVE_FONT_DIAGNOSTIC_V378.bin/.cue`는 정상입니다.
원래 38트랙 구성이며 추가 39번 트랙은 없습니다.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며, 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

v0.707 결과 BIN SHA-256:

```text
D70F2F204FA1B43828CEF22AF9F6CB233B1451BB2EA3942968697A4E6868DEA6
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
릴리스 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.707-patch -OutputDirectory C:/path/to/output
```

실제 게임이 적재한 코드와 글꼴 16KB를 첫 한글 시점에서 검사합니다.
검사 직전에 글꼴을 재설치하지 않습니다. v0.706도 실기에서는 동일 실패가 보고됐습니다.
에뮬레이터 정상/고의 손상 대조 및 EXE 적용 검사를 수행했습니다.
상세 내용과 제한은 [릴리스 노트](../RELEASE_NOTES-v0.707.md)를 참고하세요.
