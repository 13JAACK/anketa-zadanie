import pytest
from razminka.wordcount import chastota
@pytest.fixture
def fayl_s_tekstom(tmp_path):
    put = tmp_path / "text.txt"
    put.write_text(
        "Мама мыла раму. Рама, мама, рама!",
        encoding="utf-8"
    )
    return put
def test_kolichestvo_slov(fayl_s_tekstom):
    result = chastota(fayl_s_tekstom)
    assert result["мама"] == 2
    assert result["рама"] == 2
def test_net_znakov_prepinaniya(fayl_s_tekstom):
    result = chastota(fayl_s_tekstom)
    assert "рама," not in result
    assert "раму." not in result
def test_kolichestvo_raznyh_slov(fayl_s_tekstom):
    result = chastota(fayl_s_tekstom)
    assert len(result) == 4