
from rest_framework import serializers

from .models import Product, Promotion, Category, ProductImage

class PromotionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'active', 'discount', 'products_count', 'created_at', 'updated_at']
    

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'title', 'products_count']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

  
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    price_after_promotions = serializers.SerializerMethodField(
    read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'category', 'promotions', 'price_after_promotions', 'images']
   

    def get_price_after_promotions(self, product: Product):
        discount =  sum([ promotion.discount for promotion in product.promotions.all() if promotion.active])
        return product.unit_price - (discount * product.unit_price) / 100

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']




