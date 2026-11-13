import pytest

from load_scores import load_scores

def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_일부러_틀린_테스트():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 99

def test_빈_줄이_섞여있을때():
    kept, skipped = load_scores("scores_with_empty_lines.csv")
    assert len(kept) == 5
    assert len(skipped) == 0






def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores_comma.csv")
    assert len(skipped) == 1

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")

def test_헤더만_있으면_빈_결과():
    assert load_scores("scores_header_only.csv") == ([], [])

@pytest.mark.parametrize("파일, 남는수", [
    ("scores_0.csv", 1),
    ("scores_100.csv", 1),
    ("scores_101.csv", 0),
])
def test_점수_경계값(파일, 남는수):
    kept, skipped = load_scores(파일)
    assert len(kept) == 남는수






def 쓰기(파일, 내용):
    with open(파일, "w", encoding="utf-8") as f:
        f.write(내용)

쓰기("scores.csv", "이름,점수\n김하나,88\n이민준,92\n박서연,75\n최지호,60\n정수빈,100\n")
쓰기("scores_with_empty_lines.csv", "이름,점수\n김하나,88\n\n이민준,92\n\n박서연,75\n최지호,60\n정수빈,100\n")
쓰기("scores_comma.csv", "이름,점수\n김,민준,85\n")
쓰기("scores_header_only.csv", "이름,점수\n")
쓰기("scores_0.csv", "이름,점수\n김민준,0\n")
쓰기("scores_100.csv", "이름,점수\n김민준,100\n")
쓰기("scores_101.csv", "이름,점수\n김민준,101\n")

쓰기("scores_no_score.csv", "이름,점수\n김민준,\n박서연,abc\n")
쓰기("scores_no_name.csv", "이름,점수\n,85\n")

def test_점수가_비었으면_건너뛴다():
    kept, skipped = load_scores("scores_no_score.csv")
    assert len(skipped) == 2

def test_이름이_비었으면_건너뛴다():
    kept, skipped = load_scores("scores_no_name.csv")
    assert len(skipped) == 1