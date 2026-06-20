import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    """
    Рекурсивно виводить структуру директорії.
    Директорії показуються синім кольором, файли — зеленим.
    """

    items = sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1

        if is_last:
            branch = "┗ "
            next_indent = indent + "   "
        else:
            branch = "┣ "
            next_indent = indent + "┃  "

        if item.is_dir():
            print(indent + branch + Fore.BLUE + f"📂 {item.name}" + Style.RESET_ALL)
            print_directory_structure(item, next_indent)
        else:
            print(indent + branch + Fore.GREEN + f"📜 {item.name}" + Style.RESET_ALL)


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: потрібно передати шлях до директорії.")
        print("Приклад запуску:")
        print("python hw03.py C:\\Users\\xxjus\\Desktop\\picture")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        return

    if not directory_path.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
        return

    print(Fore.YELLOW + f"📦 {directory_path.name}" + Style.RESET_ALL)
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()