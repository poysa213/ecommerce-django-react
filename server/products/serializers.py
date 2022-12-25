
from rest_framework import serializers

from .models import Product, Promotion, Category

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'active', 'discount', 'products_count', 'created_at', 'updated_at']
    products_count = serializers.IntegerField(read_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'category', 'promotions', 'price_after_promotions']
    promotions = PromotionSerializer()
    price_after_promotions = serializers.SerializerMethodField(
    read_only=True)

    def get_price_after_promotions(self, product: Product):
        # summ = 0
        # for promotion in product.promotions.all():
        #     if promotion.active:
        #         summ += promotion.discount

        discount =  sum([ promotion.discount for promotion in product.promotions.all() if promotion.active])
        return product.unit_price - (discount * product.unit_price) / 100

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']

  

