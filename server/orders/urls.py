from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('carts', views.CartViewSet)

cart_routers = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_routers.register('items', views.CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + cart_routers.urls

