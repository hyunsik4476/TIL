from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies.order_by('-pk'),
    }

    return render(request, 'movies/index.html', context)


def new(request):
    genres = ['코미디', '로맨스', '공포']
    context = {
        'genres': genres,
    }

    return render(request, 'movies/new.html', context)


def create(request):
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()

    return redirect('movies:index')


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()

    return redirect('movies:index')


def edit(request, pk):
    genres = ['코미디', '로맨스', '공포']
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie': movie,
        'genres': genres,
    }

    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()

    return redirect('movies:detail', movie.pk)