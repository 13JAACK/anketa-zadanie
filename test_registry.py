import pytest

from registry import Registry

@pytest.fixture
def zhurnal_s_anketami(tmp_path):
    put = tmp_path / "ankety.txt"

    put.write_text(
        "s;Яковлев Иван;yakovlev@mail.ru;89211112233;09с34\n"
        "t;Ёлкин Пётр;elkin@mail.ru;89222223344;Кафедра И9\n"
        "s;Абрамов Алексей;abramov@mail.ru;89233334455;09с35\n"
        "x;Неизвестный Человек;bad@mail.ru;89211112233;09с34\n"
        "s;Неполная Анкета;bad@mail.ru\n"
        "s;Плохая Почта;badmail.ru;89211112233;09с34\n",
        encoding="utf-8"
    )

    zhurnal = Registry()
    zhurnal.load(put)

    return zhurnal
def test_pustoy_zhurnal():
    zhurnal = Registry()
    assert len(zhurnal) == 0
def test_kolichestvo_anket(zhurnal_s_anketami):
    assert len(zhurnal_s_anketami) == 3
def test_kolichestvo_braka(zhurnal_s_anketami):
    assert len(zhurnal_s_anketami.bad) == 3
def test_nomera_braka(zhurnal_s_anketami):
    numbers = [item[0] for item in zhurnal_s_anketami.bad]
    assert numbers == [4, 5, 6]
def test_otsutstvuyushchiy_fayl(tmp_path):
    zhurnal = Registry()
    result = zhurnal.load(tmp_path / "net.txt")
    assert result is False
def test_statistika_rolei(zhurnal_s_anketami):
    assert zhurnal_s_anketami.role_stats() == {
        "студент": 2,
        "преподаватель": 1
    }
def test_statistika_grupp(zhurnal_s_anketami):
    assert zhurnal_s_anketami.group_stats() == {
        "09с34": 1,
        "09с35": 1
    }
def test_perebor_zhurnala(zhurnal_s_anketami):
    spisok = []

    for person in zhurnal_s_anketami:
        spisok.append(person.fio)

    assert len(spisok) == 3
def test_sortirovka(zhurnal_s_anketami):
    fio = [person.fio for person in zhurnal_s_anketami]

    assert fio == [
        "Абрамов Алексей",
        "Ёлкин Пётр",
        "Яковлев Иван"
    ]
def test_save_ok(zhurnal_s_anketami, tmp_path):
    put = tmp_path / "ok.txt"

    zhurnal_s_anketami.save_ok(put)

    stroki = put.read_text(encoding="utf-8").splitlines()
    assert len(stroki) == 3
def test_save_errors(zhurnal_s_anketami, tmp_path):
    put = tmp_path / "errors.txt"

    zhurnal_s_anketami.save_errors(put)

    text = put.read_text(encoding="utf-8")
    assert "неизвестный тип" in text or "неизвестный" in text