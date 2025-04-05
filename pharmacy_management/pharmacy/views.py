from django.shortcuts import render
from rest_framework import viewsets
from .models import medicine
from .serializers import MedicineSerializer
from rest_framework.permissions import IsAuthenticated

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]
