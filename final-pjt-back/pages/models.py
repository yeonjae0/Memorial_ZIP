# Create your models here.
from django.db import models
from django.conf import settings

class Page(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_pages')
    # user.article_set().all -> 해당 유저가 작성한 모든 게시글 조회 & user가 좋아요 누른 모든 글 구별이 안된다
    # 따라서 역참조 매니저를 이름 바꿔야 된다!
    title = models.CharField(max_length=100)  # 개별 페이지 제목
    content = models.TextField()  # html 파일 string 그대로 들어올 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''
page.user : 게시글을 작성한 유저 (N:1)
user.page_set : 유저가 작성한 게시글 역참조 (N:1)
page.like_users: 게시글을 좋아요한 유저 (M:N) 
user.like_pages: 유저가 좋아요한 페이지 역참조 (M:N)
'''

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이 댓글을 단 유저 정보
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    # 이 댓글이 달린 page에 대한 정보
    # comment_set -> 해야 역참조된다
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)