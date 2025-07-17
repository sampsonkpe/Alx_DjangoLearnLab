# CREATE OPERATIONS

## Create an Author
>>> from relationship_app.models import Author
>>> author1 = Author.objects.create(name="Chinua Achebe")

## Create a Book linked to Author
>>> from relationship_app.models import Book
>>> book1 = Book.objects.create(title="Things Fall Apart", author=author1)

## Create a Library and link Book
>>> from relationship_app.models import Library
>>> library1 = Library.objects.create(name="Accra City Library")
>>> library1.books.add(book1)

## Create a Librarian linked to Library
>>> from relationship_app.models import Librarian
>>> librarian1 = Librarian.objects.create(name="Mr. Mensah", library=library1)

