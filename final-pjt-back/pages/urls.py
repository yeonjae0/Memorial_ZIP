from django.urls import path
from pages import views

urlpatterns = [
    path('pages/', views.page_list),  # 전체 페이지 조회, 페이지 생성
    path('pages/<int:page_pk>/', views.page_detail),  # 개별 페이지 조회, 수정, 삭제
    path('pages/<int:page_pk>/likes/', views.likes),  # 페이지 좋아요
    path('pages/<int:page_pk>/comments/', views.comment_list),  # 전체 댓글 조회, 댓글 생성
    path('comments/<int:comment_pk>/', views.comment_detail),  # 개별 댓글 조회, 수정, 삭제
]
