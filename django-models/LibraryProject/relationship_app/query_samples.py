# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name} library:")
    for book in books:
        print(f"- {book.title}")

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    try:
        librarian = library.librarian
        print(f"Librarian for {library.name} library: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library.name} library.")

# --- Sample Execution (Uncomment to run) ---

# books_by_author("Chinua Achebe")
# books_in_library("Accra City Library")
# librarian_for_library("Accra City Library")

