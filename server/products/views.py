from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
# from rest_framework.pa



from .serializers import ProductSerializer, CategorySerializer, PromotionSerializer
from .models import Product, Category, Promotion
from .filters import ProductFilter
from .pagination import DefaultPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unite_price', 'last_update']
    pagination_class = DefaultPagination
   
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(products_count=Count('products')).all()
    serializer_class = CategorySerializer

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.annotate(products_count=Count('products')).all()
    serializer_class = PromotionSerializer
  

    


       
