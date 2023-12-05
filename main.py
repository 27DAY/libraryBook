from classLibrary import User,Books,IssuedBooks

_books:str


while True:
    _books = f"1 - Анна Каренина{' ' * 12}4 - Дуброский\n2 - Война и Мир{' ' * 12}5 - Вишневый сад\n3 - Мертвые души{' ' * 12}6 -Выход"
    choice = input(_books)
    if choice in ["1", "2", "3", "4", "5"]:
        print('Выбор сделан')
    elif choice == "6":
        break
    else:
        continue