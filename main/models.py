from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Actors(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=55, choices=(('male', 'male'), ('female', 'female')))
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, null=True, blank=True)
    year = models.SmallIntegerField(null=True, blank=True)
    actors = models.ManyToManyField(Actors)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.TextField()
    rate = models.FloatField(validators=[MinValueValidator(0.0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.name

