import pytest
from people import Person, Student, Teacher, AnketaError, parse_line

@pytest.mark.parametrize("fio, expected", [
    ("иванов иван", "Иванов Иван"),
    ("  ИВАНОВ   ИВАН ПЕТРОВИЧ ", "Иванов Иван Петрович"),
    ("смирнова екатерина", "Смирнова Екатерина"),
    ("ПЕТРОВ ПЁТР", "Петров Пётр"),
    ("петров-водкин кузьма", "Петров-Водкин Кузьма")
])
def test_fio_normalization(fio, expected):
    assert Person.check_fio(fio) == expected
def test_fio_one_word():
    with pytest.raises(AnketaError):
        Person.check_fio("Иванов")
@pytest.mark.parametrize("mail", [
    "IVANOV@mail.ru",
    "PETROV@YANDEX.RU"
])
def test_mail_lowercase(mail):
    assert Person.check_mail(mail) == mail.lower()
@pytest.mark.parametrize("mail", [
    "ivanovmail.ru",
    "ivanov@@mail.ru",
    "ivanov@mail",
    "ivanov@.ru",
    "iv anov@mail.ru"
])
def test_bad_mail(mail):
    with pytest.raises(AnketaError):
        Person.check_mail(mail)

@pytest.mark.parametrize("phone", [
    "+7 (921) 111-22-33",
    "8 921 111 22 33",
    "79211112233",
    "+7-921-111-22-33"
])
def test_phone_normalization(phone):
    assert Person.check_phone(phone) == "79211112233"


@pytest.mark.parametrize("phone", [
    "123",
    "+69211112233",
    "abcdefghijk"
])
def test_bad_phone(phone):
    with pytest.raises(AnketaError):
        Person.check_phone(phone)
def test_masked_phone():
    person = Person("Иванов Иван", "ivanov@mail.ru", "89211112233")
    assert person.masked_phone() == "+7 (921) ***-**-33"
def test_short_fio():
    person = Person(
        "Иванов Иван Петрович",
        "ivanov@mail.ru",
        "89211112233"
    )
    assert person.short_fio() == "Иванов И. П."
def test_student_role():
    student = Student(
        "Иванов Иван",
        "ivanov@mail.ru",
        "89211112233",
        "09с34"
    )
    assert student.role() == "студент"
def test_teacher_role():
    teacher = Teacher(
        "Петров Пётр",
        "petrov@mail.ru",
        "89211112233",
        "Кафедра И9"
    )
    assert teacher.role() == "преподаватель"
def test_student_without_group():
    with pytest.raises(AnketaError):
        Student(
            "Иванов Иван",
            "ivanov@mail.ru",
            "89211112233",
            ""
        )
def test_parse_student():
    person = parse_line(
        "s;Иванов Иван;ivanov@mail.ru;89211112233;09с34"
    )
    assert isinstance(person, Student)


def test_parse_teacher():
    person = parse_line(
        "t;Петров Пётр;petrov@mail.ru;89211112233;Кафедра И9"
    )
    assert isinstance(person, Teacher)


@pytest.mark.parametrize("line", [
    "x;Иванов Иван;ivanov@mail.ru;89211112233;09с34",
    "s;Иванов Иван;ivanov@mail.ru",
    ""
])
def test_bad_line(line):
    with pytest.raises(AnketaError):
        parse_line(line)