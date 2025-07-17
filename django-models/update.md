from relationship_app.models import Book

book = Book.objects.get(title="Things Fall Apart")
book.title = "Things Still Fall Apart"
book.save()

Book.objects.get(id=book.id)

