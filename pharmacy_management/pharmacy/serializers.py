from rest_framework import serializers
from .models import medicine

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields = '__all__'

