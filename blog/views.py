
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article, Comment
from user.models import User
from prac.permissions import TOUser
from datetime import datetime, timedelta, date
from django.utils import timezone


class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [TOUser]
    
    def get(self, request):
        user = request.user
        # articles = Article.objects.filter(user=user)
        # articles = Article.objects.filter(start_date__gte=timedelta(days=3)).order_by("-start_date")
        # end_date가 현재시간보다 크다 => 기간이 남았다, 현재시간기준으로 노출종료일보다 크면 게시일 역순으로 추력
        articles = Article.objects.filter(end_date__lte=timezone.now()).order_by("-start_date")
        # titles = [article.title for article in articles] # list 축약 문법
        titles = []
        for article in articles:
            titles.append(article.title)
        return Response({"article_list": titles})
    
    def post(self, request):
        user = request.user
        title = request.data.get("title","")
        contents = request.data.get("contents","")
        categorys = request.data.get("category","")
        
        if len(title) <= 5:
            return Response({"error":"타이틀은 5자 이상 작성하셔야 합니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(contents) <= 20:
            return Response({"error":"내용은 20자 이상 작성하셔야 합니다"}, status=status.HTTP_400_BAD_REQUEST)
            
        if not categorys:
            return Response({"error":"카테고리를 등록하셔야 합니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        article = Article(
            user=user,
            title=title,
            contents=contents
        )
        article.save()
        article.category.add(*categorys)
        return Response({"작성완료"}, status=status.HTTP_200_OK)



class CommentsView(APIView):
    permission_classes = [TOUser]
    
    def post(self, request):
        user = request.user
        contents = request.data.get("contents", "")
        article = Article.objects.get(id=id)
        
        comment = Comment(
            user=user,
            contents=contents,
            article=article
        )
        comment.save()
        return Response({"댓글작성"}, status=status.HTTP_200_OK)
                
    

