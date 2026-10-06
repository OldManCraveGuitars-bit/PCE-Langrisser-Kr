# Windows 원클릭 패처

`PCE-Langrisser-Kr-v0.702-Patcher.exe`는 원본 게임이나 BIOS를 포함하지 않습니다.
배포된 v0.702 BPS·CUE만 실행 파일에 넣었습니다.

1. EXE를 실행하고 본인이 보유한 일본 원본 ISO를 선택합니다.
2. 결과 폴더를 확인하고 `검사 후 패치 적용`을 누릅니다.
3. 완료되면 결과 폴더의 `.cue`를 에뮬레이터에서 엽니다.

원본 ISO는 수정하지 않습니다. 크기·SHA-256과 BPS CRC가 맞지 않으면
적용하지 않습니다. 적용 후 단일 BIN·CUE를 다시 검증합니다.
약 560 MB의 결과 파일용 여유 공간이 필요합니다. 다른 버전의 파일이
같은 위치에 있으면 덮어쓰지 않고 중단합니다.

지원 원본 SHA-256:
`ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`

결과 BIN SHA-256:
`069EAC1E5F761C53647F94BD96C0D66CA58FD2799F014A933E3E90FF74054E4D`

내부 구현은 Python 표준 라이브러리의 BPS 적용기이며, 원본 데이터는
선택된 위치에서 읽기 전용으로 엽니다. PyInstaller로 Windows EXE를
만들 수 있습니다. 빌드에는 같은 릴리스 ZIP에서 추출한 BPS·CUE가
필요합니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.702-patch -OutputDirectory C:/path/to/output
```

v0.702는 게임 본문과 39번 트랙의 데이터를 바꾸지 않고 **단일 BIN**에
합친 원인 분리용 시험판입니다. 이전 버전의 CUE·Track39와 섞지 마세요.
[Turbo EverDrive Pro 실기에서 보고된 1화 진입 문제](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/2)의
해결 여부는 아직 확인되지 않았습니다. v0.701은 같은 증상이 재현됐습니다.
