from django.urls import path

from .views import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categorys', CategoryViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('products', ProductViewSet.as_view(), name='products'),
#     path('product/<int:pk>', ProductViewSet.as_view(), name='product'),

#     path('categorys', CategoryViewSet, name='categorys'),
#     path('category/<int:pk>', CategoryViewSet, name='category'),
# ]