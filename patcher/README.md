# Windows 원클릭 패처

`PCE-Langrisser-Kr-v0.704-Patcher.exe`는 원본 게임이나 BIOS를 포함하지 않습니다.
배포된 v0.704 BPS·CUE만 실행 파일에 넣었습니다.

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
`C995D8FBA3D88A51AEF7C13848742CF493E1D6412E72C5D8F5C71C483C53CCC9`

내부 구현은 Python 표준 라이브러리의 BPS 적용기이며, 원본 데이터는
선택된 위치에서 읽기 전용으로 엽니다. PyInstaller로 Windows EXE를
만들 수 있습니다. 빌드에는 같은 릴리스 ZIP에서 추출한 BPS·CUE가
필요합니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.704-patch -OutputDirectory C:/path/to/output
```

v0.704는 추가 39번 트랙 없이 **원래 38트랙 구성**을 유지하는 실기 시험판입니다.
로컬 V373 시험판과 동일한 BIN을 생성하며, 내부 파일명에 V373이 표시되는 것이 정상입니다.
v0.703의 데이터 배치를 유지하면서 ADPCM RAM 읽기 준비 함수의 제어 신호
해제 순서만 바꿨습니다. 9바이트 함수 중 6바이트와 해당 섹터의 EDC/ECC가 변경됐습니다.
이전 버전의 CUE·Track39와 섞지 말고, 이전 세이브스테이트 없이 새로 부팅하세요.
[Turbo EverDrive Pro 실기에서 보고된 1화 진입 문제](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/2)의
해결 여부는 아직 확인되지 않았습니다. v0.701·v0.702·v0.703은 같은 증상이 보고됐습니다.
이 버전의 에뮬레이터 검사는 실기 해결이나 전체 게임 검수를 뜻하지 않습니다.
