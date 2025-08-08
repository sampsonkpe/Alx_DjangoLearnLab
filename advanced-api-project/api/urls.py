from django.urls import path
from .views import (
    BookListCreateView, BookRetrieveUpdateDestroyView,
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book-detail-view'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

