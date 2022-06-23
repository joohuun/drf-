from functools import partial
from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from prac.permissions import TOUser
from product.serializers import ProductSerializer
from .models import Product, Review
from datetime import datetime
from django.db.models import Q
from rest_framework.views import APIView
from django.db.models import Avg


# APIView 사용
class ProductView(APIView):
    def get(self, request):
        today = datetime.now()
        products = Product.objects.filter(Q(start_date__lte=today, end_date__gte=today,) |
                                         Q(user=request.user))
        product_serailzer = ProductSerializer(products, many=True).data
        return Response(product_serailzer, status=status.HTTP_200_OK)
    

    def post(self, request):
        request.data['user'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)
        product_serializer = ProductSerializer(product ,data=request.data, partial=True)
        # partial = True ==> 부분적로 수정가능하게 함
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# ViewSet 사용
# class ProductView(viewsets.ModelViewSet):
#     permission_classes = [TOUser]
#     today = datetime.now()    
#     queryset = Product.objects.filter(start_date__lte=today, end_date__gte=today)                                       
#     serializer_class = ProductSerializer
   
#     def perform_create(self, serializer):
#         # queryset = Product.objects.all()
#         # if queryset.exists():
#         #     raise ValidationError('중복된 제품입니다.')       
#         serializer.save(user=self.request.user)
            
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


class ReviewView(APIView):
    
    def get(self, request):
        latest = Review.objects.get().
        reviews = Review.objects.all().aggregate(Avg('rate'))
        return reviews

    # def post(self, request):
    #     return         

    # def put(self, request):
    #     return     