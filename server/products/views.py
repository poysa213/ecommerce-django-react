from django.db.models.aggregates import Count

from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .serializers import ProductSerializer, CategorySerializer, PromotionSerializer
from .models import Product, Category, Promotion

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(products_count=Count('products')).all()
    serializer_class = CategorySerializer

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.annotate(products_count=Count('products')).all()
    serializer_class = PromotionSerializer
  

    


       
