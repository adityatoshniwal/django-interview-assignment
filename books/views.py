from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Book
from .serializers import BookSerializer, BookCreateSerializer
from users.permissions import IsLibrarian
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post', 'delete', 'put', 'options', 'head']

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['create', 'destroy']:
            permissions.append(IsLibrarian)
            permissions = [IsLibrarian]

        return [p() for p in permissions]

    @extend_schema(request=BookCreateSerializer)
    def create(self, request, *args, **kwargs):
        if "status" not in request.data:
            request.data['status'] = 'AVAILABLE'
        return super().create(request, *args, **kwargs)

    @action(methods=['PUT'], detail=True, name="Borrow book")
    def borrow(self, request, pk=None):
        instance = self.get_object()
        if instance.status == 'BORROWED':
            return Response({"message": "Book already borrowed"}, status=status.HTTP_400_BAD_REQUEST)
        instance.status = 'BORROWED'
        instance.save()
        return Response({}, status=status.HTTP_200_OK)

    @action(methods=['PUT'], detail=True, name="Make book book",)
    def available(self, request, pk=None):
        instance = self.get_object()
        if instance.status == 'AVAILABLE':
            return Response({"message": "Book already available"}, status=status.HTTP_400_BAD_REQUEST)
        instance.status = 'AVAILABLE'
        instance.save()
        return Response({}, status=status.HTTP_200_OK)