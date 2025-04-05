from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

