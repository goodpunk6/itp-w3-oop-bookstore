class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books
        
    def search_books(self, title = None, author = None):
        listobooks = []
        for book in self.books:
            if title is not None: # searching for title!
                if title.lower() in book.title.lower():
                    listobooks.append(book)
            elif author is not None:
                if author == book.author:
                    listobooks.append(book)
            elif author is not None and title is not None:
                if author == book.author and title.lower() in book.title.lower():
                    listobooks.append(book)
        return listobooks
            
    def add_book(self, book):
        self.books.append(book)
        


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []

    def get_books(self):
        return self.books
        

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        

