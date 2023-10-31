from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    payment_intent = models.CharField(max_length=250,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',)


    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount / 100
        
        return 0
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price / 100