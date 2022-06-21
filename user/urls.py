from django.urls import path 
from . import views 


urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    path('', views.UserView.as_view()),
    path('<obj_id>', views.UserView.as_view()),
]
