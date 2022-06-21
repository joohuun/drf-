
from django.urls import path, include
from . import views 
from .views import CommentsView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('comment', CommentsView, basename='comment') # (댓글)

urlpatterns = [
    path('article/', views.ArticleView.as_view()), 
    # path('comment/', views.CommentsView.as_view()),
    path('', include(router.urls)),    
]
