from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin

from .models import Cart,CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        return CartItem.objects.filter( \
            cart_id=self.kwargs['cart_pk']) \
                .select_related('product')
    