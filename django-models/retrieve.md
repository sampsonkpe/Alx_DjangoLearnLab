# Retrieve Operations

## All Authors
>>> Author.objects.all()
<QuerySet [<Author: Chinua Achebe>]>

## Get specific Author
>>> Author.objects.get(name="Chinua Achebe")
<Author: Chinua Achebe>

## All Books
>>> Book.objects.all()
<QuerySet [<Book: Things Fall Apart>]>

## Get Books by Author
>>> author = Author.objects.get(name="Chinua Achebe")
>>> author.book_set.all()
<QuerySet [<Book: Things Fall Apart>]>

## All Libraries
>>> Library.objects.all()
<QuerySet [<Library: Accra Central Library>]>

## Books in a Library
>>> library = Library.objects.get(name="Accra Central Library")
>>> library.books.all()
<QuerySet [<Book: Things Fall Apart>]>

## Librarian of a Library
>>> library.librarian
<Librarian: Mr. Mensah>

