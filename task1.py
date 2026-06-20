def total_salary(path):
    """
    Читає файл із зарплатами розробників і повертає
    загальну суму зарплат та середню зарплату.

    Формат рядка у файлі:
    Ім'я Прізвище,зарплата
    """

    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")

                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    except ValueError:
        print("Помилка у форматі даних у файлі")
        return 0, 0