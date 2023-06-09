from django.db import models
# from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)






# class Genre(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)

# class Movie(models.Model):
#     # genre_id = models.ManyToManyField(Genre) #related_name='movie_genre')
#     # movie_id = models.IntegerField(primary_key=True)
#     genre_id = models.IntegerField()
#     overview = models.TextField(blank=True)
#     popularity = models.FloatField()
#     poster_path = models.CharField(max_length=200, blank=True)
#     release_date = models.DateField()
#     title = models.CharField(max_length=100)
#     # video = models.BooleanField()
#     vote_average = models.FloatField()
#     vote_count = models.IntegerField()