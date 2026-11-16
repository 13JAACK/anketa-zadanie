
class AnketaError(Exception):
    pass


class Person:
    def __init__(self, fio, mail, phone):
        self.fio = self.check_fio(fio)
        self.mail = self.check_mail(mail)
        self.phone = self.check_phone(phone)

    @staticmethod
    def check_fio(raw):
        parts = raw.split()

        if len(parts) < 2:
            raise AnketaError("в ФИО меньше двух слов")

        return " ".join(p.title() for p in parts)

    @staticmethod
    def check_mail(raw):
        mail = raw.strip().lower()

        if mail.count("@") != 1:
            raise AnketaError("почта неверная: " + mail)

        left, right = mail.split("@")

        if not left or not right:
            raise AnketaError("почта неверная: " + mail)

        if "." not in right:
            raise AnketaError("почта неверная: " + mail)

        if right.startswith(".") or right.endswith("."):
            raise AnketaError("почта неверная: " + mail)

        return mail

    @staticmethod
    def check_phone(raw):
        digits = "".join(ch for ch in raw if ch.isdigit())

        if len(digits) != 11:
            raise AnketaError(
                "телефон: нужно 11 цифр, получено " + str(len(digits))
            )

        if digits[0] not in "78":
            raise AnketaError("телефон: должен начинаться с 7 или 8")

        if digits[0] == "8":
            digits = "7" + digits[1:]

        return digits

    def masked_phone(self):
        return "+7 (" + self.phone[1:4] + ") ***-**-" + self.phone[-2:]

    def short_fio(self):
        parts = self.fio.split()
        result = parts[0] + " " + parts[1][0] + "."

        if len(parts) >= 3:
            result += " " + parts[2][0] + "."

        return result

    def role(self):
        return "человек"

    def extra(self):
        return "-"

    def group_key(self):
        return None

    def __str__(self):
        return self.fio

    def __lt__(self, other):
        return self.fio < other.fio


class Student(Person):
    def __init__(self, fio, mail, phone, group):
        super().__init__(fio, mail, phone)

        group = group.strip().lower().replace(" ", "")

        if not group:
            raise AnketaError("пустая группа")

        self.group = group

    def role(self):
        return "студент"

    def extra(self):
        return self.group

    def group_key(self):
        return self.group


class Teacher(Person):
    def __init__(self, fio, mail, phone, department):
        super().__init__(fio, mail, phone)

        department = department.strip()

        if not department:
            raise AnketaError("пустая кафедра")

        self.department = department

    def role(self):
        return "преподаватель"

    def extra(self):
        return self.department


def parse_line(line):
    fields = line.split(";")

    if len(fields) != 5:
        raise AnketaError(
            "полей должно быть пять (их " + str(len(fields)) + ")"
        )

    kind = fields[0].strip().lower()

    if kind == "s":
        return Student(fields[1], fields[2], fields[3], fields[4])

    if kind == "t":
        return Teacher(fields[1], fields[2], fields[3], fields[4])

    raise AnketaError("неизвестный тип: " + kind)
