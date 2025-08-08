from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One",
            author="Author One",
            publication_year=2000
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author="Author Two",
            publication_year=2010
        )

        self.list_url = reverse('book-list-create')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_create_book(self):
        """Ensure we can create a new book."""
        data = {
            "title": "Book Three",
            "author": "Author Three",
            "publication_year": 2020
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Book Three")

    def test_list_books(self):
        """Ensure we can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Ensure we can retrieve a book."""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        """Ensure we can update a book."""
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Ensure we can delete a book."""
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        response = self.client.get(self.list_url, {'author': 'Author One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == 'Author One' for book in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book One' in book['title'] for book in response.data))

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

