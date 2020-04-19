from rest_framework import serializers
from products.models import ProductItem


class ProductItemListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductItem

        # fields = "__all__"
        fields = ['id', 'item_name', 'image_url', 'sell_price_per_item']

    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.item_image.url
        return request.build_absolute_uri(photo_url)

class ProductItemIndivSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductItem
        fields = "__all__"
