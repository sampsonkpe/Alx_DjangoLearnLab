from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book, Library

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    output = "\n".join([str(book) for book in books])
    return HttpResponse(output)

# Class-Based View to show library detail
class LibraryDetailView(View):
    def get(self, request, pk):
        try:
            library = Library.objects.get(pk=pk)
            return HttpResponse(f"Library: {library.name}")
        except Library.DoesNotExist:
            return HttpResponse("Library not found", status=404)

