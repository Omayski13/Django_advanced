from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_rest.books_api.models import Book
from django_rest.books_api.serializers import BookSerializer


# Create your views here.


class ListBookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books ,many=True)
        return Response({'books':serializer.data})

    def post(self,request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DetailBooksView(APIView):
    @staticmethod
    def get_book(pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request,book_pk):
        book = self.get_book(book_pk)
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,book_pk):
        book = self.get_book(book_pk)
        serializer = BookSerializer(book,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,book_pk):
        book = self.get_book(book_pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)