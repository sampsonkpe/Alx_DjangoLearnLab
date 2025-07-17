# Delete Operation

## Code Run in Django Shell

```python
from relationship_app.models import Book

book = Book.objects.get(title="Things Still Fall Apart")
book.delete()

