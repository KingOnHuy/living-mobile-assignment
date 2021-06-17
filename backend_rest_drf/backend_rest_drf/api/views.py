from store.models import Store
from rest_framework import viewsets
from store.serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
