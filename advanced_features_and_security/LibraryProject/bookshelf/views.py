from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book
from .forms import BookForm, ExampleForm

# View Books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    List all books with permission check.
    Uses Django ORM to safely query data, avoiding SQL injection.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Create Book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """
    Create Book view with permission check.
    Uses Django forms to validate input and protect against SQL injection.
    CSRF protection is enforced via middleware and template tokens.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


# Edit Book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    Edit Book view with permission check.
    Uses Django forms and ORM for safe update operations.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})


# Delete Book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    Delete Book view with permission check.
    Confirms deletion via POST request to prevent accidental deletes.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


# Example Form View to demonstrate secure input handling
def example_form_view(request):
    """
    Example form view demonstrating secure form handling using ExampleForm.
    Validates and sanitizes user input to prevent injection attacks.
    CSRF token protection enabled via middleware and template.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safely process cleaned data here
            data = form.cleaned_data.get('search_query')
            # Perform necessary action with data
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
