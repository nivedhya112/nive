from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)

def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})

def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form, 'movie': movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect ('/')
    return render(request,'delete.html')