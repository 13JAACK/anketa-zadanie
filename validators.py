def normalize_fio(raw):
    parts = raw.split()
    if len(parts) < 2:
        return None, "в ФИО меньше двух слов"
    fio = " ".join(p.title() for p in parts)
    return fio, None


def check_mail(raw):
    mail = raw.strip().lower()
    if mail.count("@") != 1:
        return None, "почта неверная: " + mail
    left, right = mail.split("@")
    if not left or not right:
        return None, "почта неверная: " + mail
    if "." not in right:
        return None, "почта неверная: " + mail
    if right.startswith(".") or right.endswith("."):
        return None, "почта неверная: " + mail
    return mail, None


def check_phone(raw):
    digits = "".join(ch for ch in raw if ch.isdigit())
    if len(digits) != 11:
        return None, "телефон: нужно 11 цифр, получено " + str(len(digits))
    if digits[0] not in "78":
        return None, "телефон: должен начинаться с 7 или 8"
    if digits[0] == "8":
        digits = "7" + digits[1:]
    return digits, None


def check_group(raw):
    group = raw.strip().lower().replace(" ", "")
    if not group:
        return None, "пустая группа"
    return group, None


def mask_phone(digits):
    return "+7 (" + digits[1:4] + ") ***-**-" + digits[-2:]


def parse_line(line):
    fields = line.split(";")
    if len(fields) != 4:
        return None, "полей не четыре (их " + str(len(fields)) + ")"

    fio, err = normalize_fio(fields[0])
    if err:
        return None, err

    mail, err = check_mail(fields[1])
    if err:
        return None, err

    phone, err = check_phone(fields[2])
    if err:
        return None, err

    group, err = check_group(fields[3])
    if err:
        return None, err

    return {"fio": fio, "mail": mail, "phone": phone, "group": group}, None