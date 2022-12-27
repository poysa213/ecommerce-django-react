from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('categories', views.CategoryViewSet)
router.register('promotions', views.PromotionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', views.ProductImageViewSet, basename='product-images')
urlpatterns = router.urls + products_router.urls
