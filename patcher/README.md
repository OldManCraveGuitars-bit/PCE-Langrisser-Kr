# Windows 원클릭 패처 v0.708

**게임 실행용 글꼴 읽기 수정 시험판이며, 사용자로부터 v0.708 실기 구동 성공이 보고됐습니다.**
v0.707과 달리 진단 화면에서 멈추지 않습니다. 기존 한국어판과 저장 파일은 보존하세요.

전체 시나리오 클리어와 모든 실기 구성의 검증 완료를 뜻하지 않습니다.
성공이 보고된 EXE와 패치 파일은 교체하지 않았습니다. EXE 및 ZIP 내부의
‘실기 미확인’ 안내는 최초 배포 당시 문구이며, 이후 결과는
[갱신된 릴리스 설명](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/releases/tag/v0.708)을 참고하세요.

`PCE-Langrisser-Kr-v0.708-Patcher.exe`에는 BPS 차분과 CUE만 포함됩니다.
게임 원본과 BIOS는 배포하지 않습니다.

1. EXE를 실행하고 본인 소유의 지원 일본 원본 ISO를 선택합니다.
2. 별도 결과 폴더를 지정하고 `검사 후 게임 시험 이미지 만들기`를 누릅니다.
3. 생성된 BIN과 CUE를 같은 폴더에 복사한 뒤 CUE로 새로 부팅합니다.
4. 이전 버전 세이브스테이트는 불러오지 마세요.
5. 타이틀 RUN → 시작 메뉴 글씨 → 새 게임 → 1화 설명 → 조건 화면 → 지도·대사를 확인하세요.
   글자 깨짐이나 BIOS 복귀가 남으면 화면과 직전 조작을 알려 주세요.

내부 파일명 `LANGRISSER_KR_EXPLICIT_PAIR_V379.bin/.cue`는 정상입니다.
원래 38트랙 구성이며 추가 39번 트랙은 없습니다.

원본은 읽기 전용으로 검사합니다. 크기·SHA-256·BPS CRC가 맞지 않으면
적용하지 않으며, 결과 BIN·CUE도 검증합니다. 기존 결과 파일은 덮어쓰지 않습니다.
출력용으로 약 560 MB의 여유 공간이 필요합니다.

지원 원본 SHA-256:

```text
ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68
```

v0.708 결과 BIN SHA-256:

```text
8D5EAD72A5BAD9A5817AC50595D2E4BC32E91273CB517A0053EF0A063A3F0B60
```

Python 표준 라이브러리의 BPS 적용기를 PyInstaller로 묶었습니다.
릴리스 ZIP의 BPS·CUE로 다음과 같이 빌드할 수 있습니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.708-patch -OutputDirectory C:/path/to/output
```

연속 읽기 의존을 줄인 V379 게임을 생성합니다. 이전 패치판이 아닌 일본 원본에 적용하세요.
실제 EXE 적용 결과 해시, 원본 보존, 기존 출력 덮어쓰기 거부, 잘못된 원본 거부를
검사했습니다. 상세 내용과 제한은 [릴리스 노트](../RELEASE_NOTES-v0.708.md)를 참고하세요.
