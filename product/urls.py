from django.urls import path
from rest_framework import routers

from .views import ProductViewSet, CategoryViewSet


router = routers.SimpleRouter()

router.register(r'products', ProductViewSet)
router.register(r'categorys', CategoryViewSet)

urlpatterns = router.urls