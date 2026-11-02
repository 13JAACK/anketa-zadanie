from validators import mask_phone


def print_report(good, bad, total):
    good.sort(key=lambda a: a["fio"])

    print(f"{'№':<4}{'ФИО':<30}{'Почта':<25}{'Телефон':<22}{'Группа':<8}")
    print("-" * 90)

    for i, a in enumerate(good, 1):
        print(f"{i:<4}{a['fio'][:28]:<30}{a['mail'][:23]:<25}"
              f"{mask_phone(a['phone']):<22}{a['group']:<8}")

    print()
    print("Отклонено строк:", len(bad))
    for num, raw, reason in bad:
        print("строка", num, ":", reason)
        print("   ", raw)

    print()
    print("Всего строк в файле:", total)
    print("Принято:", len(good), "| Отклонено:", len(bad))

    stat = {}
    for a in good:
        stat[a["group"]] = stat.get(a["group"], 0) + 1

    print("По группам:")
    for g in sorted(stat):
        print(g, stat[g])