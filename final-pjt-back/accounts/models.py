from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# pjt06 참고
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    # 좋아요한 아티클(게시글/페이지)
    


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    # media/image/ 아래에 저장하는 방식 (미리 저장해둘까?)
    profile_img = models.ImageField(upload_to='image')
