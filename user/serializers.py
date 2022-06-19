from rest_framework import serializers
from user.models import User, Profile, Hobby


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ["name"]
        

class ProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)   # 유저프로필과 취미는 매니투매니 관계
    class Meta:
        model = Profile
        fields = ["introduction", "birthday", "age", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()   # 유저프로필과 유저는 원투원 관계
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email", "profile"]
        # fields = "__all__"
        
    