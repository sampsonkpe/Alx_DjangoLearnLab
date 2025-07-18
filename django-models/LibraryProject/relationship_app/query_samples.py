from .models import Book, Library

# 1. List all books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 2. Query all books by a specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author=author_name)

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None

