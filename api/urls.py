from django.urls import path

from .views import (GenreListCreateAPIView, GenreDetailAPIView,
                    BookListCreateAPIView, BookDetailAPIView)

urlpatterns = [
    path('genres/', GenreListCreateAPIView.as_view()),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view()),

    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]