
from registry import Registry


INPUT_FILE = "anketa.txt"


def main():
    registry = Registry()

    if not registry.load(INPUT_FILE):
        print("Файл", INPUT_FILE, "не найден")
        return

    print(f"{'№':<4}{'ФИО':<30}{'Роль':<16}"
          f"{'Группа/кафедра':<22}{'Телефон':<22}")
    print("-" * 94)

    for number, person in enumerate(registry.people, 1):
        print(
            f"{number:<4}{person.fio[:28]:<30}"
            f"{person.role():<16}{person.extra():<22}"
            f"{person.masked_phone():<22}"
        )

    print("-" * 94)

    print("Принято:", len(registry))
    print("Отклонено:", len(registry.bad))

    print("\nСтатистика по ролям:")
    for role, count in sorted(registry.role_stats().items()):
        print(role + ":", count)

    print("\nСтатистика по группам:")
    for group, count in sorted(registry.group_stats().items()):
        print(group + ":", count)

    print("\nПричины отклонения:")
    for number, raw, reason in registry.bad:
        print("Строка", number, ":", reason)
        print("Данные:", raw)

    registry.save()
    print("\nРезультаты сохранены в ok.txt и errors.txt")


if __name__ == "__main__":
    main()
