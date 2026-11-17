
from people import parse_line, AnketaError


class Registry:
    def __init__(self):
        self.people = []
        self.bad = []

    def add(self, person):
        self.people.append(person)

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            return False

        for number, line in enumerate(lines, 1):
            if not line.strip():
                continue

            try:
                person = parse_line(line.rstrip("\n"))
                self.add(person)
            except AnketaError as error:
                self.bad.append((number, line.strip(), str(error)))

        self.people.sort(
            key=lambda person: person.fio.lower().replace("ё", "е")
        )
        return True

    def __len__(self):
        return len(self.people)

    def __iter__(self):
        return iter(self.people)

    def role_stats(self):
        result = {}

        for person in self.people:
            role = person.role()
            result[role] = result.get(role, 0) + 1

        return result

    def group_stats(self):
        result = {}

        for person in self.people:
            group = person.group_key()

            if group is not None:
                result[group] = result.get(group, 0) + 1

        return result

    def save(self):
        with open("ok.txt", "w", encoding="utf-8") as file:
            for person in self.people:
                file.write(
                    person.role() + ";"
                    + person.fio + ";"
                    + person.mail + ";"
                    + person.masked_phone() + ";"
                    + person.extra() + "\n"
                )

        with open("errors.txt", "w", encoding="utf-8") as file:
            for number, raw, reason in self.bad:
                file.write(
                    "Строка " + str(number) + ": " + reason + "\n"
                )
                file.write(raw + "\n\n")
    def save_ok(self, filename="ok.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for person in self.people:
                file.write(
                    person.role() + ";"
                    + person.fio + ";"
                    + person.mail + ";"
                    + person.masked_phone() + ";"
                    + person.extra() + "\n"
                )
    def save_errors(self, filename="errors.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for number, raw, reason in self.bad:
                file.write(
                    "Строка " + str(number) + ": " + reason + "\n"
                )
                file.write(raw + "\n\n")