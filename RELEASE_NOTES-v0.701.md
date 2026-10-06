![PCE 랑그릿사 한국어판 메인 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/title.png)

# PCE-Langrisser-Kr v0.701 — 실기 호환성 시험판

v0.7에서 보고된 Turbo EverDrive Pro + PC Engine GT의 화면·글자 깨짐 및
시나리오 진입 중 재시작 문제를 좁히기 위한 프리릴리스입니다. **실기에서
해결됐다고 확인된 버전은 아닙니다.** [실기 제보와 사진](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/1)을 참고해 주세요.

## v0.7 대비 변경

- 별도 39번 데이터 트랙을 `MODE1/2048`의 23개 섹터(47,104바이트)에서
  `MODE1/2352`의 23개 섹터(54,096바이트)로 다시 구성했습니다. 데이터
  2,048바이트와 트랙 번호·위치는 유지하고 각 섹터에 헤더와 EDC/ECC를 넣었습니다.
- CUE의 39번 트랙 선언과 파일명을 새 형식에 맞췄습니다. 본편 BIN 및 BPS는
  v0.7과 바이트 단위로 같습니다. 번역 문장과 그림 데이터는 바꾸지 않았습니다.
- 수동 BPS ZIP과 Windows 패처 EXE 모두 새 CUE·39번 트랙을 동봉합니다.
  이전 버전의 BIN·CUE·트랙 파일을 섞지 마세요.

## 검사 결과와 한계

- 원본 일본판에서 BPS 적용한 본편 BIN의 SHA-256:
  `8F722CAF1E8B5EB871AFA7394E65850B241E6A0740381E35633D2D7FCBBD0851`.
- 새 39번 트랙은 23개 `MODE1/2352` 섹터의 헤더·EDC·ECC를 검증했습니다.
- v0.7과 v0.701을 같은 에뮬레이터 단축 경로에서 각 60,000회 갱신하며
  비교했습니다. 주요 RAM·VRAM 스냅샷 6개, CD 읽기·재생 및 실행 감시
  기록이 일치했습니다. 이것은 실제 플레이 전수 검사나 실기 호환성 보증이 아닙니다.
- Turbo EverDrive Pro + GT에서 제보된 깨짐·재시작이 해결되는지, 다른
  실기·ODE에서 정상 동작하는지는 **미검증**입니다. 문제 발생 시 장비,
  실행 방법, 깨지는 첫 화면과 CUE 선택 여부를 [이슈 1](https://github.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/issues/1)에 남겨 주세요.
- v0.7의 알려진 번역·그래픽 검수 한계는 그대로입니다.
  [v0.7 릴리스 노트](RELEASE_NOTES-v0.7.md)를 확인해 주세요.

## 적용

본인 소유 일본 원본 ISO(SHA-256
`ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`)를
준비하고 EXE 또는 ZIP의 BPS로 패치하세요. 완성 BIN은 동봉 CUE·Track39와
같은 폴더에 둔 뒤 **CUE**를 여세요. 원본 게임 이미지와 BIOS는 배포하지
않습니다. 기존 세이브스테이트 자동 불러오기를 끄고 새로 부팅하세요.
