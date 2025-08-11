from django.urls import path
from .views import (
    RegisterView, ProfileView, edit_profile, CustomLoginView, CustomLogoutView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

app_name = 'blog'

urlpatterns = [
    # Auth
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),

    # Blog CRUD
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

