# 성적 관리 프로그램

## 무엇을 하나요 (What)
성적 CSV 파일을 읽어서 유효한 (이름, 점수)만 골라 내고, 건너뛴 줄은 이유와 함께 기록합니다.

## 왜 만들었나요 (Why)
실제 성적 파일에는 점수가 빈 칸이거나, 101처럼 범위 밖이거나, 이름이 비어 있는 줄이 섞여 있어서
그냥 읽으면 프로그램이 중간에 죽습니다. 그런 줄을 버리지 않고 "몇 행이 왜 빠졌는지" 남기기 위해 만들었습니다.

## 어떻게 쓰나요 (How)
pip install pytest pytest-cov
python load_scores.py scores.csv

## 어떻게 테스트하나요
pytest test_load_scores.py -v
→ 10 passed (정상 3 · 예외 2 · 경계값 3 · 빈 값 2)
pytest --cov=load_scores --cov-report=term-missing test_load_scores.py
→ 커버리지 80% (남은 77-86은 직접 실행용 코드)

## 파일 구성
- load_scores.py : 성적 CSV를 읽는 함수 (시험 대상)
- test_load_scores.py : 내가 작성한 pytest 테스트
- test_ai_A.py / test_ai_B.py : AI에게 코드·명세를 주고 받은 테스트 (고치지 않음)
- bug3_logic.py / test_ai_C_버그.py : 버그 코드와 AI가 만든 테스트 (함정 확인용)
- prompts.txt : AI에게 보낸 프롬프트 원문
- scores*.csv : 테스트가 자동으로 만드는 입력 파일

## 만든 사람
최서윤 (학번: 2026100194) · 미래융합학부 자율전공
AI는 테스트 설계표 정리, 커버리지 결과 해석, test_ai_A/B/C 생성에 사용했고 load_scores.py와 Why 칸은 직접 썼습니다.