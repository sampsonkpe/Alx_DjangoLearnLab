from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library

# Function-based view to list books
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        books = Book.objects.filter(library=library).select_related('author')
        return render(request, 'relationship_app/library_detail.html', {
            'library': library,
            'books': books
        })

