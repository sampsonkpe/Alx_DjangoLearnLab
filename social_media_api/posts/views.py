from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at', 'title']

    def get_queryset(self):
        return Post.objects.select_related('author').annotate(
            comments_count=Count('comments')
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        qs = Comment.objects.filter(post_id=pk).select_related('author')
        page = self.paginate_queryset(qs)
        ser = CommentSerializer(page if page is not None else qs, many=True)
        if page is not None:
            return self.get_paginated_response(ser.data)
        return Response(ser.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['post', 'author']
    search_fields = ['content']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        return Comment.objects.select_related('post', 'author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

