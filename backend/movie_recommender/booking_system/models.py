from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CAST_TYPE = [(1, "actor"), (2, "director"), (3, "producer")]
GENDERS = [(1, "male"), (2, "female"), (3, "other")]
LANGUAGES = [(0, "english"), (1, "hindi"), (2, 'telugu')]


class Language(models.Model):
    lang = models.CharField(max_length=100, unique=True)

class Cast(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField(default=0)
    gender = models.IntegerField(choices=GENDERS)
    link = models.TextField(default="")
    description = models.TextField(default="")
    cast_type = models.IntegerField(choices=CAST_TYPE)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre


class UserProfile(User):
    age = models.IntegerField(default=0)
    gender = models.IntegerField(choices=GENDERS)
    phone = models.CharField(default="", max_length=10)
    genre_pref = models.ManyToManyField(Genre)


class Movie(models.Model):
    title = models.CharField(max_length=100, default="")
    synopsis = models.TextField(default="")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    casts = models.ManyToManyField(Cast)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class SeatType(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0)


class Theater(models.Model):
    name = models.CharField(max_length=100, default="")
    location_lat = models.FloatField(default=0)
    location_long = models.FloatField(default=0)
    seat_types = models.ManyToManyField(SeatType)


class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=10, default="")


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    time = models.TimeField()


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    seat_identifier = models.CharField(max_length=100, default="")
    show  = models.ForeignKey(Show, on_delete=models.CASCADE)
    type = models.ForeignKey(SeatType, on_delete=models.CASCADE)


class Invoice(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket_price = models.FloatField(default=0)
    taxes = models.FloatField(default=0)
    service_charge = models.FloatField(default=0)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    description = models.TextField(default="")

