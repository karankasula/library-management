from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.library.models import Book, Library   
from apps.library.api.serializers import BookSerializer, LibrarySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.query_params.get('q', None)
        print("query", query)
        if query:
            queryset = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        print("Query set", queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def search(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        test = Book.objects.filter(title__icontains="Ram")
        print("------test----->>>", test)
        queryset = self.get_queryset().filter(Q(title__icontains=query) | Q(author__icontains=query))
        print("queryset--", queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer