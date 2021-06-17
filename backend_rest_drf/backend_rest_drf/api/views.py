from store.models import Store, Category
from rest_framework import viewsets
from store.serializers import StoreSerializer, CategorySerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category
