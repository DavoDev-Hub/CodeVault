from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 1,
            'title': 'Inception',
            'director': 'Christopher Nolan',
            'year': 2010
        },
        {
            'id': 2,
            'title': 'The Matrix',
            'director': 'The Wachowski Brothers',
            'year': 1999
        },
        {
            'id': 3,
            'title': 'Interstellar',
            'director': 'Christopher Nolan',
            'year': 2014
        },
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")