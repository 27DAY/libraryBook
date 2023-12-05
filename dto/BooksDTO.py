from classLibrary.Books import Books
def GetAllBooks():
    books = Books.select().dicts()
    returnBooks = []
    for book in books:
        returnBooks.append(Books(id = book["id"],name = book["name"],size = book["size"],price = book["price"]))
    return returnBooks
def GetBooksById(Id:int):
    book = Books.select().where(Books.id == Id).get()
    return book
