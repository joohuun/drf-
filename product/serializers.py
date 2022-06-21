from django.forms import ValidationError
from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if '제목' not in data['name']:
            raise ValidationError('제목이 들어가야 합니다')
        print(data)
        return data
    
    class Meta:
        model = Product
        fields = ["user", "name", "image", "dec",
                  "registered_date", "start_date", "end_date"]
        
        
        
