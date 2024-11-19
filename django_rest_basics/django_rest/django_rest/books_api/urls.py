from django_rest.books_api.views import ListBookView, DetailBooksView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', ListBookView.as_view(),name='books'),
    path('books/<int:book_pk>/', DetailBooksView.as_view(),name='books'),
]
