>>> from relationship_app.models import Book
>>> book = Book.objects.get(title="Discipleship 101")
>>> book.delete()
(1, {'relationship_app.Book': 1})
>>> from relationship_app.models import Book
>>> Book.objects.all()
<QuerySet [<Book: The Call to Purpose>]>

