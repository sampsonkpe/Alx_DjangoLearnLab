from relationship_app.models import Book, Author, Library

# List all books in a library
library = Library.objects.get(name="Central Library")
books = library.books.all()

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
author_books = Book.objects.filter(author=author)

# Retrieve the librarian for a library
library_name = "Central Library"
librarian = Library.objects.get(name=library_name).librarian

