from razminka.calc import summa, skidka, srednee
import pytest
def test_summa_polozhitelnye():
    assert summa(2, 3) == 5
def test_summa_s_nulem():
    assert summa(0, 7) == 7
def test_skidka_10_procentov():
    assert skidka(1000, 10) == 900
def test_skidka_slishkom_bolshaya():
        import pytest
        with pytest.raises(ValueError):
            skidka(1000, 95)
def test_srednee_pustogo_spiska():
        import pytest
        with pytest.raises(ValueError):
            srednee([])
@pytest.mark.parametrize("chisla, expected", [
    ([5], 5),
    ([2, 4], 3),
    ([1, 2, 3, 4], 2.5),
    ([-2, 2], 0)
])
def test_srednee(chisla, expected):
    assert srednee(chisla) == expected