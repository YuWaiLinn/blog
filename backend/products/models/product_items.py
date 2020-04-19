from django.conf import settings
from django.db import models
# from django.utils import timezone

class ProductItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default=0)
    buy_price_per_item = models.IntegerField(default=0)
    sell_price_per_item = models.IntegerField(default=0)
    sell_price_above_5 = models.IntegerField(default=0)
    sell_price_above_10 = models.IntegerField(default=0)

    item_image = models.ImageField(upload_to='products_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="created_by", on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="updated_by", on_delete=models.SET_NULL, null=True)

    def sell_price(self, item_count):
        if (item_count > 10):
            return self.sell_price_above_10 / 10
        if (item_count > 5):
            return self.sell_price_above_5 / 5
        else:
            return self.sell_price_per_item

    def __str__(self):
        return self.item_name
