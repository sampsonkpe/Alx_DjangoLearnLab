from relationship_app.models import Library, Author, Book

# --- List all books in a library ---
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(books)

# --- Query all books by a specific author ---
author_name = "Some Author"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# --- Retrieve the librarian for a library ---
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print(librarian)

