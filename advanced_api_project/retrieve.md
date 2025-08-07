# Retrieve Book Records

# All books
Book.objects.all()

# Get book by ID
Book.objects.get(id=1)

# Filter by author
Book.objects.filter(author="James Clear")

