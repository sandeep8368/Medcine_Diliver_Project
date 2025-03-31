from django.urls import path,include
from rest_framework.routers import DefaultRouter
from orders.views import MedicineViewSet, OrderViewSet


router = DefaultRouter()
router.register(r'medicnes',MedicineViewSet)
router.register(r'orders',OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]