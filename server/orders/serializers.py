
from django.core.validators import MinValueValidator
from django.db import transaction
from rest_framework import serializers


from .models import Cart, CartItem
from products.models import Product
from products.serializers import SimpleProductSerializer
from .models import Order, OrderItem
from users.models import Customer

class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']

class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer(
        validators=[MinValueValidator(1)]
    )
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'updated_at', 'items', 'total_price']


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        if not Product.objects.filter(pk=product_id).exists():
            raise serializers.ValidationError('No product with the given ID was found')
        return product_id
    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        cart_id = self.context['cart_id']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
  

    # def validate_product_id(self, product_id):
    #     if not Product.objects.filter(pk=product_id).exists():
    #         raise serializers.ValidationError('No product with the given ID was found')
    #     return product_id

    class Meta:
        model = CartItem
        fields = ['quantity']

class OrderItemSerialzer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'unite_price', 'quantity']

class OrderSerialzer(serializers.ModelSerializer):
    items = OrderItemSerialzer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']

class UpdateOrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']
        

class CreateOrderSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField()
  
    def validat_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart ')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty')
        return cart_id

    def save(self):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            (customer, created) = Customer.objects.get(user_id=self.context['user_id'])
            order = Order.objects.create(customer=customer)

            cart_items = CartItem.objects. \
                select_related('product') \
                .filter(cart_id=cart_id)
            order_items = [
                OrderItem(
                    order=order, 
                    product=item.product,
                    unite_price=item.product.unite_price,
                    quantity=item.quantity
                ) for item in cart_items
                ]
            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk=cart_id).delete()
            return Order
