from relationship_app.models import Book, Author, Publisher, Librarian, Library

# Sample query: Get all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(authors=author)
print(f"Books by {author.name}:", books_by_author)

# Sample query: Get the publisher of a specific book
book = Book.objects.get(title="The Django Way")
print(f"Publisher of {book.title}:", book.publisher.name)

# Sample query: Get all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = Book.objects.filter(library=library)
print(f"Books in {library.name}:", books_in_library)

# Sample query: Get librarian of a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}:", librarian.name)

# Sample query: Get libraries managed by a specific librarian
librarian = Librarian.objects.get(name="Sampson")
libraries_managed = Library.objects.filter(librarian=librarian)
print(f"Libraries managed by {librarian.name}:", libraries_managed)

