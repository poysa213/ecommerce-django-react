from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('promotion', views.PromotionViewSet)

urlpatterns = router.urls