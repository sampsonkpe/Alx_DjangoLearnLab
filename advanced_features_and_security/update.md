>>> from relationship_app.models import Book
>>> book = Book.objects.get(title="The Call to Purpose")
>>> book.publication_year
2020
>>> book.publication_year = 2021
>>> book.save()
>>> book
<Book: The Call to Purpose>
>>> book.publication_year
2021

