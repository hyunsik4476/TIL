import logging
from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)



def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'form': form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.user == request.user:
            movie.delete()
    return redirect('movies:index')

@login_required
def update(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance = movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def comment_create(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
    return redirect('movies:detail', movie.pk)
    

@require_POST
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk= comment_pk)
    if request.user.is_authenticated:
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', pk)