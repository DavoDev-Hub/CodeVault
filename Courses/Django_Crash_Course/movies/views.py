from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
    movie_list = Movie.objects.all()
    data = {'movies': movie_list}
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(id=id)
    return render(request, 'movies/detail.html', {'movie': data})