from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View (FBV)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

