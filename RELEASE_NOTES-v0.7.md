![PCE 랑그릿사 한국어판 메인 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/title.png)

# PCE-Langrisser-Kr v0.7 — 한국어 패치 프리릴리스

PC Engine CD-ROM²판 《랑그릿사: 광휘의 후예》의 개인 테스트용 한국어
패치입니다. 공개 버전은 **v0.7**, 내부 빌드는 **V369**입니다. 원본 게임과
BIOS를 포함하지 않는 BPS 패치 묶음을 제공합니다. 아직 최종 완성판이
아니므로 아래 검수 범위와 알려진 문제를 읽고 사용해 주세요.

## 이번 공개판에 들어간 내용

1. **한국어 화면과 대사:** 한국어 타이틀, 메뉴, 인물·직업 표기, 일반/초
   랑그 시나리오 대사 데이터를 통합했습니다. 한글화 크레딧 표기는
   `기타 깎는 노인`입니다. 번역 데이터의 존재와 모든 대사 분기의 실제
   플레이 검증은 별개입니다.
2. **게임 내부 영상 자막:** 오프닝과 중간 영상의 한국어 자막을 게임 안에
   표시합니다. 오프닝, 영상보기 1번, 15번의 그림 간섭을 수정하고 일본
   원판과 각각 5,488장, 5,336장, 1,987장의 출력 프레임을 대조했습니다.
   이 세 구간의 결과를 다른 모든 영상의 전수 검사로 확대하지 않습니다.
3. **엔딩 B 후일담 수정:** 영상보기에서 엔딩 B를 열면 한글 글꼴 적재를
   건너뛰어 후일담 본문이 모자이크처럼 깨졌습니다. B 선택 경로에만 글꼴
   적재를 선행하고 원래 음원 호출을 유지했습니다. 깨졌던 첫 후일담 화면은
   수정본에서 정상 표시됨을 확인했습니다.
4. **전환·저장 시험:** V368에서 일반 1→2, 2→3, 3→4화의 종료·저장·다음
   화 진입을 격리된 단축 조건으로 확인했습니다. V369는 여기에 B 전용
   수정을 추가한 판이며, 전체 자연 전투 완주를 뜻하지 않습니다.
5. **패치 무결성:** BPS를 지원 원본에 다시 적용해 V369 BIN과 SHA-256이
   정확히 일치함을 확인했습니다. 제품의 MODE1 섹터 5,304개도 검사했습니다.

## 실제 화면

| 일반 1화 대사 | 지휘관 배치 |
| --- | --- |
| ![일반 1화 대사](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/scenario-1-dialogue.png) | ![지휘관 배치](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/deployment.png) |

| 일반 2화 대사 | 오프닝 자막 |
| --- | --- |
| ![일반 2화 대사](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/scenario-2-dialogue.png) | ![오프닝 자막](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/opening-subtitle.png) |

영상보기 엔딩 B의 수정 후 첫 후일담 화면:

![엔딩 B 후일담](https://raw.githubusercontent.com/OldManCraveGuitars-bit/PCE-Langrisser-Kr/main/screenshots/ending-b-epilogue.png)

## 적용 방법

1. 본인 소유의 일본 원본 ISO를 준비합니다. 지원 원본 SHA-256:
   `ECE10A51AABD107E7F4B83DACA1DEC7B3B0B43D7C15FCFBAE89E840C77910E68`
2. 첨부 ZIP을 풀고 BPS 도구로 `.bps`를 원본 ISO에 적용합니다.
3. 결과 이름을 `LANGRISSER_KR_VISUAL_ENDING_B_FONT_V369_TECH.bin`으로 둡니다.
4. 결과 BIN, 동봉 CUE, 추가 Track39 BIN을 같은 폴더에 둡니다.
5. 에뮬레이터에서 **CUE**를 열어 실행합니다. PC Engine CD-ROM² BIOS는
   별도 준비해야 합니다. 이전 빌드의 세이브스테이트 자동 복원은 끄세요.

결과 BIN SHA-256:
`8F722CAF1E8B5EB871AFA7394E65850B241E6A0740381E35633D2D7FCBBD0851`

## 현재 알려진 문제

- 일반 1화 하단 직업/이름 줄에 금색 타일이 섞이는 표시 오류가 있습니다.
- 엔딩 B의 첫 후일담 본문은 확인했지만, 사용자가 보고한 알베르트 화면을
  포함한 모든 후일담 장면을 직접 캡처해 전수 대조한 것은 아닙니다.
- 일반·초 랑그 1~20화의 자연 플레이 완주, 모든 분기·영상·효과음의 최신
  빌드 전수 검증은 끝나지 않았습니다. 테스트 중 새 오류가 발견될 수 있습니다.

원본 게임 이미지, BIOS, 사용자 저장 파일은 첨부하지 않았습니다.
서로 다른 버전의 BIN·CUE·트랙을 섞지 마세요.
