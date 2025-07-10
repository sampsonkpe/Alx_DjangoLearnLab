# CRUD Operations for Book Model

## Create
from bookshelf.models import Book  
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)  
book  
# Output: <Book: 1984 by George Orwell (1949)>

## Retrieve
book = Book.objects.get(title="1984")  
book.title, book.author, book.publication_year  
# Output: ('1984', 'George Orwell', 1949)

## Update
book.title = "Nineteen Eighty-Four"  
book.save()  
book.title  
# Output: 'Nineteen Eighty-Four'

## Delete
book.delete()  
Book.objects.all()  
# Output: <QuerySet []>
