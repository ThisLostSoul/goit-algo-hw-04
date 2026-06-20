def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та аргументи.
    Команда приводиться до нижнього регістру.
    """

    parts = user_input.strip().split()

    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


def add_contact(args, contacts):
    """
    Додає новий контакт у словник.
    Формат команди: add name phone
    """

    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name.lower()] = phone

    return "Contact added."


def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    Формат команди: change name phone
    """

    if len(args) != 2:
        return "Invalid command."

    name, new_phone = args
    key = name.lower()

    if key not in contacts:
        return "Contact not found."

    contacts[key] = new_phone

    return "Contact updated."


def show_phone(args, contacts):
    """
    Показує номер телефону контакту.
    Формат команди: phone name
    """

    if len(args) != 1:
        return "Invalid command."

    name = args[0]
    key = name.lower()

    if key not in contacts:
        return "Contact not found."

    return contacts[key]


def show_all(contacts):
    """
    Показує всі збережені контакти.
    """

    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()