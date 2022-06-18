from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, logout, authenticate

from user.models import Profile

def sum_numbers(*args, **kwargs):
    return sum(args)


class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = request.user # 로그인한 사용자를 user에 담는다.
        
        # 역참조를 사용한 경우
        profile = user.profile
        # hobbys = user.profile.hobby.all()  # user모델.profile모델.hobby
        # hobbys = str(hobbys)
        
    
        # # 역참조를 사용하지 않았을 경우
        # profile = Profile.objects.get(user=user)
        # hobbys = user.profile.hobby.all()
        
        return Response({'message': str(profile) })
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
    
    
class UserAPIView(APIView):
    def post(self, request):
        username = request.data.get('username','')
        password = request.data.get('password','')
        
        user = authenticate(request, username=username, password=password)
        
        if not user:
            return Response({"error":"존재하지 않는 계정이거나 패스워드가 일치하지 않습니다"}, status=status.HTTP_401_UNAUTHORIZED)
        
        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공"})
    

    

        
        

