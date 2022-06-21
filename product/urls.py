from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductView


router = DefaultRouter()
router.register('', ProductView, basename='product') 


urlpatterns = [
    path('', include(router.urls)),    
]