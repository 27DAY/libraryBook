from classLibrary.User import User
from classLibrary.Books import Books
from classLibrary.IssuedBooks import IssuedBooks


if __name__ == "__main__":
    status = "OK"
    try:
        User.drop_table()
        Books.drop_table()
        IssuedBooks.drop_table()

    except Exception as e:
        status = f"Drop error, {e}"
    try:
        User.create_table()
        Books.create_table()
        IssuedBooks.create_table()

    except Exception as e:
        status = f"Create error, {e}"
    print(f"Migration {status}")