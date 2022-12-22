from django_filters.rest_framework import FilterSet
from .models import Product 


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category__id': ['exact'],
            'unit_price': ['gt', 'lt']
        }
