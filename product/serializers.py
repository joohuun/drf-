from django.forms import ValidationError
from rest_framework import serializers
from .models import Product, Review
from datetime import datetime



class ProductSerializer(serializers.ModelSerializer):
    
    # def validate(self, data):
    #     if '@' not in data['name']:
    #         raise ValidationError('@가 들어가야 합니다')
    #     print(data)
    #     return data
    def validate(self, data):
        today = datetime.now()
        if data['end_date'] > data[today] :
            raise serializers.ValidationError('노출종료일이 지났습니다.')
        return data
    
    class Meta:
        model = Product
        fields = ["user", "name", "image", "dec",
                  "registered_date", "start_date", "end_date"]
        
        

# class ReviewSerializer(serializers.ModelSerializer):
#     aver_rate = serializers.SerializerMethodField()
#     def get_aver_rate(self, obj):
        
    
#     class Meta:
#         model = Review
#         fileds = "__all__"
        
        
        
        
