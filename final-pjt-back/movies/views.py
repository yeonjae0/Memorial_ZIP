from django.shortcuts import render, redirect
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie, Genre
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404, get_list_or_404

import requests
import json
from django.http import JsonResponse
import random

# def get_data(request):
#     data = json.loads(request.body)
#     selected_genres = data.get('arr', [])

@api_view(['POST'])
def recommend(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(request)
    # requset.POST.get(request)
    rec_set = set()
    
    genre_ids = json.loads(request.body.decode('utf-8'))
    id1, id2 = genre_ids
    # genres = Genre.objects.get(pk=id1 or id2 or id3)
    movie_set = Movie.objects.all()
    movie_tmp1 = Movie.objects.filter(genres__id=id1)
    print(movie_tmp1)
    # titles = movie_tmp1.values_list('title','overview','posterpath', flat=True)  ## <class 'django.db.models.query.QuerySet'>
    titles = movie_tmp1.values_list('title','overview','poster_path')  ## <class 'django.db.models.query.QuerySet'>
    for title in titles:
        # print(title)
        rec_set.add(title)

    movie_tmp2 = Movie.objects.filter(genres__id=id2)
    # titles = movie_tmp2.values_list('title','overview','posterpath', flat=True)  ## <class 'django.db.models.query.QuerySet'>
    titles = movie_tmp2.values_list('title','overview','poster_path')  ## <class 'django.db.models.query.QuerySet'>
    for title in titles:
        rec_set.add(title)
    # rec_set에 영화 타이틀들이 들어갔다
    lst = random.sample(list(rec_set),2)
    print(333333333333333333333333333)
    print(lst)

    context = {
        # 'message': 'data 처리완료',
        'rec_lst' : lst
    }
    # print(context)
    return JsonResponse(context)
    # if request.method == 'GET':























# 영화정보를 DB에 저장
# @api_view(['GET'])
# def makejson(request):
#     for page in range(1, 31):
#         # print(page)
#         response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key=40a69d93e84171e666e3a8b8cfd8acb4&language=ko-KR&page={page}')
#         if response.status_code == 200:
#             for result in response.json()['results']:
#                 #print(result)  # 영화 하나 정보
#                 res = requests.get(f"https://api.themoviedb.org/3/movie/{result['id']}/videos?api_key=40a69d93e84171e666e3a8b8cfd8acb4&language=ko-KR&page={page}")
#                 json_data = response.json()
#                 data_list = json_data['results']
#                 # print(2222)
#         for item in data_list:
#             # print(33333)
#             for i in range(len(item['genre_ids'])):
#                 movie = Movie()
#                 movie.genre_id = item['genre_ids'][i]
#                 # print('dlrpdfdsfasfdfsdaf')
#                 movie.overview = item['overview']
#                 movie.popularity = item['popularity']
#                 movie.poster_path = item['poster_path']
#                 movie.release_date = item['release_date']
#                 movie.title = item['title']
#                 movie.vote_average = item['vote_average']
#                 movie.vote_count = item['vote_count']
#                 movie.save()

# @api_view(['GET'])
# def make_genres(request):

#     response = requests.get('https://api.themoviedb.org/3/genre/movie/list?language=ko-KR&api_key=40a69d93e84171e666e3a8b8cfd8acb4')
#     genres = response.json()
#     for genre_ in genres['genres']:
#         Genre.objects.create(
#             id = genre_['id'],
#             name = genre_['name']
#         )
#     return Response(json_data)

# @api_view(['GET'])
# def make_genres(request):

#     response = requests.get('https://api.themoviedb.org/3/genre/movie/list?language=ko-KR&api_key=40a69d93e84171e666e3a8b8cfd8acb4')
#     genres = response.json()
#     for genre_ in genres['genres']:
#         Genre.objects.create(
#             id = genre_['id'],
#             name = genre_['name']
#         )