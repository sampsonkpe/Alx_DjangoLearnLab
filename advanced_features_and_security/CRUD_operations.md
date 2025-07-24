## CRUD Operations Summary

This document summarises the CRUD operations performed on the `Library`, `Author`, and `Book` models within the `relationship_app` of the `LibraryProject`.

---

###  Create

Used the Django shell to create instances of Library, Author, and Book:

```python
from relationship_app.models import Library, Author, Book

library = Library.objects.create(name="Ahavah Community Library")
author1 = Author.objects.create(name="Sampson Kpe")
author2 = Author.objects.create(name="Ama Serwaa")

book1 = Book.objects.create(title="The Call to Purpose", author=author1, library=library, publication_year=2020)
book2 = Book.objects.create(title="Discipleship 101", author=author2, library=library, publication_year=2022)

library.books.set([book1, book2])

