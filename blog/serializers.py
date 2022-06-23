from rest_framework import serializers
from .models import Article, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        

class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Comment
        fields = "__all__"
        

class ArticleSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)    
    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        # print(obj)
        # article_list = []
        # for category in obj.category.all:
        #     article_list.append(category.name)
        # return article_list    
        return [category.name for category in obj.category.all()]
    
    class Meta:
        model = Article
        fields = "__all__"
        
        
