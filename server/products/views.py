from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pa


from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer, CategorySerializer, PromotionSerializer, ProductImageSerializer
from .models import Product, Category, Promotion, ProductImage
from .filters import ProductFilter
from .pagination import DefaultPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unite_price', 'last_update']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    
   
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(products_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.annotate(products_count=Count('products')).all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


    def  get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
    
  

    


       
