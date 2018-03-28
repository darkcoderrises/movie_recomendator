from rest_framework import generics
from .serializers import CrewSerializer, CrewProfile, MovieSerializer, Movie
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
import json
#from booking_system.models import Genre
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter
#import django_filters
from itertools import chain

# Create your views here.


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env


# class CastList(generics.ListCreateAPIView):
#     queryset = Cast.objects.all()
#     serializer_class = CastSerializer
# 
# 
# class CastDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cast.objects.all()
#     serializer_class = CastSerializer
# 
# 
# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def search(request):
    movie_list = Movie.objects.all()
    #for movie in movie_list:
     #   print("<{}>".format(movie.title))
    #print(movie_list)
    movie_filter = UserFilter(request.GET, queryset=movie_list)
    #print(movie_filter.qs)
    return render(request, 'movie_list.html', {'filter': movie_filter})


def show_movies(request):
    movies = Movie.objects.all()
    #movie_list = [render_to_string("movie_thumbnail.html", MovieSerializer(movie).data) for movie in queryset]
    return render(request, 'movies.html', {'movies': movies})


def show_cast(request, cast_id):
    if request.method == "POST":
        return HttpResponse("Only supports GET request")

    cast = CrewProfile.objects.get(id=cast_id)
    cast_data = CrewSerializer(cast)

    movie_list = cast.movie_set.all()
    movie_list = [render_to_string("movie_thumbnail.html", MovieSerializer(movie).data) for movie in movie_list]

    return render(request, 'cast.html', {"cast": cast_data.data, "movies": movie_list})

def running(request):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def upcoming(request):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def payment(request):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def book_show(request, show_id):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def movie(request, movie_id):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def confirm_booking(request, show_id):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def crew(request, crew_id):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')

def theater(request, theater_id):
    return HttpResponseNotFound('<h1>Page under construction?</h1>')
