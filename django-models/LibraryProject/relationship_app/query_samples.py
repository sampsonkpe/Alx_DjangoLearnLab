from relationship_app.models import Library, Author

# --- List all books in a library ---
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(books)

# --- Query all books by a specific author ---
author_name = "Some Author"
author = Author.objects.get(name=author_name)
books = author.books.all()
print(books)

# --- Retrieve the librarian for a library ---
library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(librarian)

