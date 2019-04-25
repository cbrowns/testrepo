
from articles.models import Article

from .serializers import ArticleSerializers

from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


# from rest_framework.generics import (
#     ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView)


# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers


# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers


# class ArticleUpdateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers


# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
