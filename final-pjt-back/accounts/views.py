from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

from .models import Profile, User
from dj_rest_auth.views import LogoutView

# Create your views here.
def update_profile(request):
    if request.method == 'POST':
        image_url = request.POST.get('imageUrl')
        print(image_url)

        profile = Profile.objects.get(user=request.user)  # 사용자의 프로필 객체를 가져옴
        profile.profile_image = image_url
        profile.save()

        return JsonResponse({'message': '프로필이 업데이트되었습니다.'})
    else:
            return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(person)
    return JsonResponse(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def userinfo(request):
    # user = request.user
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    others = get_object_or_404(get_user_model(), pk=user_pk)  # 상대방들
    me = request.user  # 나: 로그인된 유저
    if me != others:
        # 다른사람과 나 팔로우였다면
        if others.followers.filter(pk=me.pk).exists():  
            others.followers.remove(me)  # 팔로우 삭제
            is_followed = False  # 팔로우 상태 False
        else:  # 팔로우가 아니었다면
            others.followers.add(me)  # 팔로우 추가하기
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followers_count': others.followers.count(),
            'followings_count': others.followings.count(), # count()는 orm                
        }
        return JsonResponse(context)
    return Response(status=status.HTTP_404_NOT_FOUND)
