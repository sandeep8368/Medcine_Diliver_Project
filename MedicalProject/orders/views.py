from rest_framework import viewsets
from orders.models import Medicine, Order
from orders.serializers import MedicineSerializer, OrderSerializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
    
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)