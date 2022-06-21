from urllib import request
from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import permissions, status, viewsets, mixins
from rest_framework.response import Response
from prac.permissions import TOUser
from product.serializers import ProductSerializer
import user
from .models import Product
from datetime import datetime
from django.db.models import Q


# Create your views here.


# class ProductView(mixins.UpdateModelMixin, 
#                 mixins.ListModelMixin, 
#                 mixins.RetrieveModelMixin,
#                 viewsets.GenericViewSet):
class ProductView(viewsets.ModelViewSet):
    permission_classes = [TOUser]
    today = datetime.now()    
    queryset = Product.objects.filter(start_date__lte=today, end_date__gte=today)                                       
    serializer_class = ProductSerializer
   
    def perform_create(self, serializer):
        # queryset = Product.objects.all()
        # if queryset.exists():
        #     raise ValidationError('중복된 제품입니다.')       
        serializer.save(user=self.request.user)
            
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    
    
        
        