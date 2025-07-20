from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register, admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Use Django's built-in views with template_name
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('register/', register, name='register'),

    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]

