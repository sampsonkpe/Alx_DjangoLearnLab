from rest_framework import serializers
from .models import Author
from .models import Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value < 1900 or value > 2100:
            raise serializers.ValidationError("Publication year must be between 1900 and 2100.")
        return value
