from django.http import HttpResponse, HttpResponseRedirect
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

def add(request):
    title = request.POST.get('title')
    director = request.POST.get('director')
    year = request.POST.get('year')

    if title and director and year:
        movie = Movie(title=title, director=director, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        movie.delete()
    except Movie.DoesNotExist:
        return HttpResponse("Movie not found", status=404)
    return HttpResponseRedirect("/movies")