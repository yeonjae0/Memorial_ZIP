from rest_framework import serializers
from .models import Page, Comment
from accounts.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('page', 'user',)

# class PageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Page
#         fields = '__all__'
#         read_only_fields = ('user',)

class PageSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    
    # 페이지에 달린 댓글들
    comment_set = CommentSerializer(many=True, read_only=True)
    # 페이지에 달린 댓글 개수
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Page
        fields = (
            'pk', 
            'user', 
            'title', 
            'content', 
            'comment_set',
            'comment_count',
            'like_users')


    