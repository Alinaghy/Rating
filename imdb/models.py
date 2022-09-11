from unittest import result
from django.contrib.auth.models import AbstractUser
from django.db import models

#---class-0--------------------------------------------------------------------------------
class User (AbstractUser):
    pass

#---class-1--------------------------------------------------------------------------------
class Actors (models.Model):
    name = models.CharField(max_length=64, default=None)
    info = models.CharField(max_length=2000, default=None)
    image = models.URLField(max_length=200, default=None)

    def __str__(self) :
        return f"{self.name}"

#---class-2--------------------------------------------------------------------------------
class Directors (models.Model):
    name = models.CharField(max_length=64, default=None)
    info = models.CharField(max_length=2000, default=None)
    image = models.URLField(max_length=200, default=None)

    def __str__(self) :
        return f"{self.name}"

#---class-3--------------------------------------------------------------------------------
class Movies (models.Model):
    Gener = [
        ('comedy','comedy'),
        ('drama','drama'),
        ('action','action'),
        ('horror','horror'),
        ('animation','animation'),
    ]
    name = models.CharField(max_length=64, default=None)
    info = models.CharField(max_length=2000, default=None)
    actors = models.ManyToManyField(Actors, related_name="actors")
    rate = models.IntegerField(default=0)
    rate_num = models.IntegerField(default=1)
    rate_user = models.ManyToManyField(User, related_name="ruser")
    result_rate = models.FloatField(default=0)
    trailer = models.URLField(max_length=200, default=None)
    image = models.URLField(max_length=200, default=None)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    gener =  models.CharField(max_length=20, choices=Gener)

    def __str__(self) :
        return f"{self.name}"

#---class-4--------------------------------------------------------------------------------
class Watchlist (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movies, related_name="item2")

    def __str__(self):
        return f"{self.user}"

#---class-5--------------------------------------------------------------------------------
class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default=None)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} : {self.comment}"

#---class-6--------------------------------------------------------------------------------
class Trend(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.movie}"