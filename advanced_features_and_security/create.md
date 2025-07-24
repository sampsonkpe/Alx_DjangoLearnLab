>>> from relationship_app.models import Library
>>> library = Library.objects.create(name="Ahavah Community Library")
>>> library
<Library: Ahavah Community Library>
>>> from relationship_app.models import Author
>>> author1 = Author.objects.create(name="Sampson Kpe")
>>> author2 = Author.objects.create(name="Ama Serwaa")
>>> author1, author2
(<Author: Sampson Kpe>, <Author: Ama Serwaa>)
>>> from relationship_app.models import Book
>>> book1 = Book.objects.create(title="The Call to Purpose", author=author1, library=library, publication_year=2020)
>>> book2 = Book.objects.create(title="Discipleship 101", author=author2, library=library, publication_year=2022)
>>> book1, book2
(<Book: The Call to Purpose>, <Book: Discipleship 101>)
>>> library.books.set([book1, book2])
>>> library.books.all()
<QuerySet [<Book: The Call to Purpose>, <Book: Discipleship 101>]>

