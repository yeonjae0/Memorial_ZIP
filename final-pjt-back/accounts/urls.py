from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update_profile/', views.update_profile),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
    path('userinfo/', views.userinfo, name='userinfo'),
    # path('make_genres/', views.make_genres),
    # path()

]