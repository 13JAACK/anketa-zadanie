from validators import parse_line
from storage import read_input, write_results
from report import print_report


def main():
    lines = read_input()
    if lines is None:
        return

    good = []
    bad = []
    total = 0

    for num, line in enumerate(lines, 1):
        if not line.strip():
            continue

        total += 1
        anketa, err = parse_line(line.rstrip("\n"))

        if err:
            bad.append((num, line.strip(), err))
        else:
            good.append(anketa)

    print_report(good, bad, total)
    write_results(good, bad)

    print("Сохранено: ok.txt и errors.txt")


if __name__ == "__main__":
    main()