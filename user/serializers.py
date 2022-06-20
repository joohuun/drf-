from matplotlib.style import context
from rest_framework import serializers
from user.models import User, Profile, Hobby
from blog.serializers import ArticleSerializer, CommentSerializer


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # print(type(obj))
        # print(dir(obj))
        # print(obj)
        user = self.context["request"].user
        print(user)
        
        user_list = []
        for profile in obj.hobby.exclude(user=user):
            user_list.append(profile.user.username)       
        return user_list
        # return [profile.user.username for profile in obj.hobby.all()]    
        
    class Meta:
        model = Hobby
        fields = ["name", "same_hobby_users"]  # 필드값에 역참조 사용가능, "hobby"="profile_set" 로 바로 불러오기가능
        

class ProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)   # 유저프로필과 취미는 매니투매니 관계
    class Meta:
        model = Profile
        fields = ["introduction", "birthday", "age", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()   # 유저프로필과 유저는 원투원 관계
    articles = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source="comment_set") 
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email", "profile", "articles", "comments"]
        # fields = "__all__"
       
        
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ["username", "password", "fullname", "email", "profile"]
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        pw = user.password
        user.set_password(pw)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        pw = user.password
        user.set_password(pw)
        user.save()
        return user
        
    