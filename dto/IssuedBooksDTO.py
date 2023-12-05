from classLibrary.IssuedBooks import IssuedBooks
def GetAllIssuedBooks():
    issued_books = IssuedBooks.select().dicts()
    returnIssuedBooks = []
    for issued_book in issued_books:
        returnIssuedBooks.append(IssuedBooks(id = issued_book["id"],name = issued_book["name"],size = issued_book["size"],price = issued_book["price"]))
    return returnIssuedBooks
def GetIssuedBooksById(Id:int):
    issued_book = IssuedBooks.select().where(IssuedBooks.id == Id).get()
    return issued_book
def RegistrationIssuedBooks():
    name = input("введите имя пользователя")
    phone = input("введите номер телефона")
    IssuedBook = IssuedBooks(name=name,phone=phone,bouns=0)
    IssuedBook.save()