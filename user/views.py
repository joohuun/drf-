from numpy import flatiter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, logout, authenticate
from django.db.models import F
from user.serializers import UserSerializer, ProfileSerializer, HobbySerializer


class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = request.user # 로그인한 사용자를 user에 담는다.
        return Response(UserSerializer(user).data)
        
        # # 역참조를 사용한 경우
        # profile = user.profile
        # hobbys = user.profile.hobby.all()  # user모델.profile모델.hobby
        # # hobbys = str(hobbys)
        # for hobby in hobbys:
		#     # exclde : 매칭 된 쿼리만 제외, filter와 반대
		#     # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
		#     # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
		#     # F() : 객체에 해당되는 쿼리를 생성함
        #     # hobby_members = hobby.profile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
        #     hobby_members = hobby.hobby.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
        #     hobby_members = list(hobby_members)
        #     print(f"hobby : {hobby.name} / hobby members : {hobby_members}")
        #     # 허비맴버 = 허비모델.프로필모델(related_name=hobby).포함(유저만포함,관리제x).필드이름을 F(유저모델__유저네임)으로변경.리스트
        #     # 결과적으로 관리자를 제외한 유저이름을 리스트로 출력, 하비모델은 프로필모델을 정참조하고 프로필모델은 하비모델를 역참조
        #     # 취미가 공통된 유저를 불러온다.  하비모델.프로필모델_SET.exclude().~~~~~
           
        # # 역참조를 사용하지 않았을 경우
        # profile = Profile.objects.get(user=user)
        # hobbys = user.profile.hobby.all()
        
        
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
    

    

        
        

