# Windows 원클릭 패처 v0.8

지휘관집중·수동과 어택·실드의 아이콘을 복구하고 상점 스크롤 지연을 줄인 시험판입니다.
v0.75의 마법명 원음 표기·페이지 화살표 수정과 v0.708의 실기 대응 읽기 방식을 포함합니다.
**v0.8의 실기 확인과 드문 마법 연출의 아이콘 영역 충돌 검수는 남아 있습니다.**

`PCE-Langrisser-Kr-v0.8-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
게임 원본과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 별도 결과 폴더를 지정하고 `검사 후 v0.8 이미지 만들기`를 누릅니다.
3. 생성된 BIN과 CUE를 같은 폴더에 두고 **CUE로 새로 부팅**합니다.
4. 이전 버전 세이브스테이트는 불러오지 마세요. 게임 내 저장 파일은 백업하세요.

내부 파일명 `LANGRISSER_KR_FIELD_MARKERS_V384.bin/.cue`는 정상입니다.
원래 38트랙 구성이며 추가 39번 트랙은 없습니다.
이전 한글 패치판이 아닌 일본 원본에 적용하세요.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

v0.8 결과 BIN SHA-256:

```text
7EA3AE0884805E55BECC1E42C0B95FCBBE10D00CE6593C27FEAE77E9CCB12436
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
릴리스 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다.

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.8-patch -OutputDirectory C:/path/to/output
```

검사 결과는 ZIP의 `patcher-test.json`, 수정 내용은
[상세 변경과 검증 범위](../RELEASE_NOTES-v0.8.md)를 참고하세요.
