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
    assert len(skipped) == 2