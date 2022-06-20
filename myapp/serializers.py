# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import *
  
# Create a model serializer 
class OrderDetailsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = OrderDetails
        fields = '__all__'