# Windows 원클릭 패처 v0.706

**게임 실행용 실기 시험판입니다. v0.705처럼 진단 화면만 나오는 버전이 아닙니다.**
실기 문제가 해결됐다고 확인한 버전은 아니므로 기존 한국어판과 저장 파일은 보존하세요.

`PCE-Langrisser-Kr-v0.706-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
게임 원본과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 별도 결과 폴더를 지정하고 `검사 후 게임 패치 적용`을 누릅니다.
3. 생성된 BIN과 CUE를 같은 폴더에 복사한 뒤 CUE로 새로 부팅합니다.
4. 이전 버전 세이브스테이트는 불러오지 마세요.
5. 타이틀 RUN → 새 게임 → 시나리오 설명 → 1화 지도까지 확인해 주세요.
   한글 글자 상태와 BIOS 리셋 여부를 알려 주세요.

내부 파일명 `LANGRISSER_KR_EXPLICIT_FONT_DEST_V375.bin/.cue`는 정상입니다.
원래 38트랙 구성이며 추가 39번 트랙은 없습니다.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며, 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

v0.706 결과 BIN SHA-256:

```text
0809452D538BC6EC289E3B664D603FE6A52BA675412BD670E2A0BA1902EF4F19
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
릴리스 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.706-patch -OutputDirectory C:/path/to/output
```

게임의 압축 글꼴 전송 설정 1바이트를 바꿔 목적지 주소를 명시합니다.
실기에서 v0.705 독립 진단은 통과했지만 실제 게임 해결은 아직 확인하지 못했습니다.
에뮬레이터의 1화 진입·전체 글꼴 전송 대조·EXE 적용 검사를 수행했습니다.
상세 내용과 제한은 [릴리스 노트](../RELEASE_NOTES-v0.706.md)를 참고하세요.
