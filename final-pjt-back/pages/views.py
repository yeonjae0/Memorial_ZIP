from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Page, Comment

from .serializers import PageSerializer, CommentSerializer
# Create your views here.


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def page_list(request):
    if request.method == 'GET':  # 전체 페이지 조회
        pages = get_list_or_404(Page)
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':  # 페이지 생성
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE']) 
def page_detail(request, page_pk):
    page = get_object_or_404(Page, pk=page_pk)
    if request.method == 'GET':
        serializer = PageSerializer(page)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def comment_list(request, page_pk):
    page = get_object_or_404(Page, pk=page_pk)
    if request.method == 'GET':  # 개별 페이지에 달린 댓글 목록
        comments = page.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':  # 페이지에 댓글 달기
        serializer =  CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(page=page, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':  # 개별 댓글 자세한 정보
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def likes(request, page_pk):
    page = get_object_or_404(Page, pk=page_pk)
    # 게시글을 좋아요한 유저 중에 요청을 보낸 유저가 있다면(이미 좋아요를 눌렀다면)
    if page.like_users.filter(pk=request.user.pk).exists():
        page.like_users.remove(request.user)  # 좋아요 취소
        is_liked = False  # 현재 request.user은 현재 페이지 좋아요를 안 누른 상태
    else:  # 좋아요 안 눌렀다면
        page.like_users.add(request.user)
        is_liked = True  # 현재 request.user은 현재 페이지 좋아요를 누른 상태
    context = {
        'is_liked': is_liked,
        'likes_count': page.like_users.count(),
    }
    return JsonResponse(context, status=status.HTTP_200_OK)
