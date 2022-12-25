
from rest_framework import serializers

from .models import Product, Promotion, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'category', 'promotions']

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']

    # price_after_promotions = serializers.SerializerMethodField(
    #     method_name='calculate_promotions')

    # def calculate_tax(self, product: Product):
    #     return product.unit_price * Decimal()

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'active', 'discount', 'products_count', 'created_at', 'updated_at', 'deleted_at']
    products_count = serializers.IntegerField(read_only=True)