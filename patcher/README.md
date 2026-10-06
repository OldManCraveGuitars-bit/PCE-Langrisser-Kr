# Windows 원클릭 패처

`PCE-Langrisser-Kr-v0.7-Patcher.exe`는 원본 게임이나 BIOS를 포함하지 않습니다.
배포된 v0.7 BPS·CUE·Track39만 실행 파일에 넣었습니다.

1. EXE를 실행하고 본인이 보유한 일본 원본 ISO를 선택합니다.
2. 결과 폴더를 확인하고 `검사 후 패치 적용`을 누릅니다.
3. 완료되면 결과 폴더의 `.cue`를 에뮬레이터에서 엽니다.

원본 ISO는 수정하지 않습니다. 크기·SHA-256과 BPS CRC가 맞지 않으면
적용하지 않습니다. 적용 후 BIN·CUE·Track39를 다시 검증합니다.
약 560 MB의 결과 파일용 여유 공간이 필요합니다. 다른 버전의 파일이
같은 위치에 있으면 덮어쓰지 않고 중단합니다.

지원 원본 SHA-256:
`ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`

결과 BIN SHA-256:
`8F722CAF1E8B5EB871AFA7394E65850B241E6A0740381E35633D2D7FCBBD0851`

내부 구현은 Python 표준 라이브러리의 BPS 적용기이며, 원본 데이터는
선택된 위치에서 읽기 전용으로 엽니다. PyInstaller로 Windows EXE를
만들 수 있습니다. 빌드에는 같은 릴리스 ZIP에서 추출한 BPS·CUE·Track39가
필요합니다:

```powershell
./patcher/build.ps1 -AssetDirectory C:/path/to/PCE-Langrisser-Kr-v0.7-patch -OutputDirectory C:/path/to/output
```

기존 수동 BPS ZIP은 그대로 이용할 수 있습니다. 이 EXE는 적용 편의 도구일 뿐,
게임 데이터나 검수 범위를 변경하지 않습니다.
[Turbo EverDrive Pro + PC Engine GT 실기에서 보고된 1화 진입 문제](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/1)도
이 EXE로 해결된 것은 아닙니다.
