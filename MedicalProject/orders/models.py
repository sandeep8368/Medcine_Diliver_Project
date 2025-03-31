from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Shipped", "Shipped"), ("Delivered", "Delivered")], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)