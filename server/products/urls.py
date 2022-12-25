from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('categories', views.CategoryViewSet)
router.register('promotions', views.PromotionViewSet)

urlpatterns = router.urls
