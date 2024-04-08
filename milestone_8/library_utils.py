from typing import List, Set

def read_books_from_file(filename):
    books = []
    with open(filename, 'r') as file:
        for line in file:
            title, author, year_published, category = line.strip().split(', ')
            # print(f"{title}, {author}, {category}, {year_published}")
            books.append((title.strip("(").strip("'"), author.strip("'"), int(year_published), category.strip(")").strip("'")))
    return books


class Book:
    def __init__(self, title: str, author: str, year: int, category: 'Category'):
        self.title = title
        self.author = author
        self.year_published = year
        self.category = category
        

    def getTitle(self) -> str:
        return self.title

    def getCategory(self) -> 'Category':
        return self.category

class Category:
    def __init__(self, name: str):
        self.name = name

    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.getName()
    
    def __eq__(self, other):
        if isinstance(other, Category):
            return self.name == other.name
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)


class Shelf:
    def __init__(self, num: int):
        self.categories = set()
        self.books: List[Book] = []
        self.number = num

    def addBook(self, book: Book):
        self.books.append(book)
        self.categories.add(book.getCategory())

    def addCategory(self, category: Category):
        self.categories.add(category)

    def sortBooksByTitle(self):
        self.books.sort(key=lambda x: (x.getCategory().getName(), x.getTitle()))

class Catalog:
    def __init__(self):
        self.shelves: List[Shelf] = []

    def addShelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def organizeBooks(self, books: List[Book]):
        for book in books:
            for shelf in self.shelves:
                if book.getCategory() in shelf.categories:
                    shelf.addBook(book)
                    break

    def sortBooksByTitle(self):
        for shelf in self.shelves:
            shelf.sortBooksByTitle()

    def __str__(self) -> str:
        res = ""
        for shelf in self.shelves:
            res += f"Shelf {shelf.number + 1}\n"
            for book in shelf.books:
                cat = f"{book.category}"
                cat_formatted = "{:^{width}}".format(cat, width=15)
                res += f"    | {cat_formatted} | {book.title} - {book.author} \n"
            res += f"\n"
        return res
