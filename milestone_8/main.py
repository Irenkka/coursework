from library_utils import Catalog, Category, Shelf, Book, read_books_from_file

# Read books from file



if __name__ == '__main__':
    raw_books = read_books_from_file("books.txt")

    # Create categories
    categories = set()
    for book in raw_books:
        cat = Category(book[-1])
        if cat not in categories:
            categories.add(cat)
    
    # Create books
    books = [Book(title, author, year, Category(category)) for (title, author, year, category) in raw_books]

    # Each shelf has two categories
    shelves = [Shelf(num) for num in range(len(categories)//2)]
    for shelf in shelves:
        if len(categories) > 1:
            shelf.addCategory(categories.pop())
            shelf.addCategory(categories.pop())
        elif len(categories) > 0:
            shelf.addCategory(categories.pop())
        else:
            break

    # Create catalog and add the shelves
    catalog = Catalog()
    for shelf in shelves:
        catalog.addShelf(shelf)
    # categories = set([cat for cat in categories])
    catalog.organizeBooks(books)
    catalog.sortBooksByTitle()

    print(f"{catalog}")



# Creating shelves
# shelf1 = Shelf()
# shelf1.addCategory(fiction)
# shelf1.addCategory(non_fiction)

# # Creating catalog
# catalog = Catalog()
# catalog.addShelf(shelf1)

# # Organizing books
# books = {book1, book2, book3, book4}
# catalog.organizeBooks(books)

# # Sorting books
# catalog.sortBooksByTitle()

# # Printing sorted books
# for shelf in catalog.shelves:
#     print(f"Shelf Categories: {[category.getName() for category in shelf.categories]}")
#     for book in shelf.books:
#         print(f"Book Title: {book.getTitle()}, Category: {book.getCategory().getName()}")