from relationship_app.models import Book, Author, Library, Librarian

# Query: List all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()

# Query: All books by a specific author
def books_by_author(author_id):
    return Book.objects.filter(author__id=author_id)

# Query: Retrieve librarian for a library
def get_librarian(library_id):
    return Librarian.objects.get(library__id=library_id)

