from django.conf import settings
from django.db import models
# from django.utils import timezone

# Product App
from products.models import ProductItem

class Order(models.Model):
    total_count = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    total_discount = models.IntegerField(default=0)
    delivery_fee = models.IntegerField(default=0)

    customer_name = models.CharField(max_length=200)
    customer_detail = models.CharField(max_length=200)

    product_item_id = models.ManyToManyField(ProductItem, through='OrderItems', related_name='OrderItems')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="order_created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="order_updated_by", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.customer_name


# Many 2 Many Table
class OrderItems(models.Model):
    product_item_id = models.ForeignKey(ProductItem, on_delete=models.SET_NULL, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    
    sell_price_per_item = models.IntegerField(default=0)
    sell_count = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.product_item_id.item_name