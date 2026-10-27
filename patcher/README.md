# Windows 원클릭 패처 v0.84

현재 소스는 내부 V398 번역 검수 반영판을 빌드합니다. 대사·표기·자막 28건을 수정했고,
필드 이름·클래스 권장 표기 9건은 작은 글꼴 공간 문제로 남아 있습니다.
v0.831의 Mesen 부팅 호환성, 38트랙 구성과 음성·효과음 데이터를 유지합니다.
**에뮬레이터 검증이며 실기 재검증은 하지 못했습니다.**

`PCE-Langrisser-Kr-v0.84-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
게임 원본과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 별도 결과 폴더를 지정하고 `검사 후 v0.84 이미지 만들기`를 누릅니다.
3. 생성된 BIN과 CUE를 같은 폴더에 두고 **CUE로 새로 부팅**합니다.
4. 이전 버전 세이브스테이트는 불러오지 마세요. 게임 내 저장 파일은 백업하세요.

내부 파일명은 `LANGRISSER_KR_TRANSLATION_V398.bin/.cue`입니다.
기존 빌드의 BIN과 새 CUE를 섞어 사용하지 마세요.
원래 38트랙 구성이며 추가 39번 트랙은 없습니다.
이전 한글 패치판이 아닌 일본 원본에 적용하세요.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

V398 결과 BIN SHA-256:

```text
64637801C457AD8A38837D1B74CC522BA9C1C5A38212B6157CD5A0F8098D17C1
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
v0.84 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다.

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/v0.84 -OutputDirectory C:/path/to/output
```

검사 결과는 ZIP의 `patcher-test.json`, `runtime-audit.json`, `translation-review.json`,
사용 방법과 수정 내용은 `README-KO.txt`를 참고하세요.
[전체 수정 내용·미반영 항목·검증 범위](../RELEASE_NOTES-v0.84.md)를 참고하세요.
