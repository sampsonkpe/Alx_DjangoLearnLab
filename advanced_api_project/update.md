# Update Book Record

book = Book.objects.get(id=1)
book.title = "Born a Crime: Stories from a South African Childhood"
book.save()

# Verify update
Book.objects.get(id=1)

