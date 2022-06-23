from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

# from product.views import ProductView

# router = DefaultRouter()
# router.register('', ProductView, basename='product') 


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ProductView.as_view()),  
    path('<obj_id>', views.ProductView.as_view()),
    path('review/', views.ReviewView.as_view()),
        
]