# Delete Book Record

book_to_delete = Book.objects.get(id=2)
book_to_delete.delete()

# Verify deletion
Book.objects.all()

