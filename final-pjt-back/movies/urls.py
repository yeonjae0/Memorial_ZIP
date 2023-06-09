from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend),
    # path('make_genres/', views.make_genres),
    # path()

]