from rest_framework import serializers
from orders.models import Medicine, Order


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
        
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'