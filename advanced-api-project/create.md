# Create Book Records

from api.models import Book

book1 = Book.objects.create(title="Born a Crime", author="Trevor Noah", pages=304)
book2 = Book.objects.create(title="Atomic Habits", author="James Clear", pages=320)

# Verify creation
Book.objects.all()

