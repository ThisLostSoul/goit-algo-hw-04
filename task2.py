def get_cats_info(path):
    """
    Читає файл з інформацією про котів і повертає список словників.

    Формат рядка у файлі:
    id,name,age
    """

    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except ValueError:
        print("Помилка у форматі даних у файлі")
        return []
cats_info = get_cats_info(r"C:\Users\xxjus\Desktop\catsinfo.txt")
print(cats_info)