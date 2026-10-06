# Windows 원클릭 패처

`PCE-Langrisser-Kr-v0.703-Patcher.exe`는 원본 게임이나 BIOS를 포함하지 않습니다.
배포된 v0.703 BPS·CUE만 실행 파일에 넣었습니다.

1. EXE를 실행하고 본인이 보유한 일본 원본 ISO를 선택합니다.
2. 결과 폴더를 확인하고 `검사 후 패치 적용`을 누릅니다.
3. 완료되면 결과 BIN과 CUE를 같은 폴더에 복사하고, 실행 장비에서 `.cue`를 엽니다.

원본 ISO는 수정하지 않습니다. 크기·SHA-256과 BPS CRC가 맞지 않으면
적용하지 않습니다. 적용 후 단일 BIN·CUE를 다시 검증합니다.
약 560 MB의 결과 파일용 여유 공간이 필요합니다. 다른 버전의 파일이
같은 위치에 있으면 덮어쓰지 않고 중단합니다.

지원 원본 SHA-256:
`ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`

결과 BIN SHA-256:
`21ABC1F4E557665C127A646408E4748B7D28EB84C99964EE224E42984E49A7A6`

내부 구현은 Python 표준 라이브러리의 BPS 적용기이며, 원본 데이터는
선택된 위치에서 읽기 전용으로 엽니다. PyInstaller로 Windows EXE를
만들 수 있습니다. 빌드에는 같은 릴리스 ZIP에서 추출한 BPS·CUE가
필요합니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.703-patch -OutputDirectory C:/path/to/output
```

v0.703은 추가 39번 트랙 없이 **원래 38트랙 구성**을 유지하는 실기 시험판입니다.
V372의 검증된 BIN을 그대로 생성하며, 내부 파일명에 V372가 표시되는 것이 정상입니다.
추가 글꼴·공급 모듈을 기존 2번 데이터 트랙으로 옮겼습니다.
이전 버전의 CUE·Track39와 섞지 말고, 이전 세이브스테이트 없이 새로 부팅하세요.
[Turbo EverDrive Pro 실기에서 보고된 1화 진입 문제](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/2)의
해결 여부는 아직 확인되지 않았습니다. v0.701과 v0.702는 같은 증상이 보고됐습니다.
