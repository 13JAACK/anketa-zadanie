from validators import mask_phone
INPUT_FILE = "anketa.txt"
OK_FILE = "ok.txt"
ERR_FILE = "errors.txt"


def read_input():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Файл", INPUT_FILE, "не найден")
        return None


def write_results(good, bad):
    with open(OK_FILE, "w", encoding="utf-8") as f:
        for a in good:
            f.write(a["fio"] + ";" + a["mail"] + ";"
                    + mask_phone(a["phone"]) + ";" + a["group"] + "\n")

    with open(ERR_FILE, "w", encoding="utf-8") as f:
        for num, raw, reason in bad:
            f.write("строка " + str(num) + ": " + reason + "\n")
            f.write(raw + "\n\n")