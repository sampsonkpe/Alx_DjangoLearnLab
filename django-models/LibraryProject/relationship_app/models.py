from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"

