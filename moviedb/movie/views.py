from django.shortcuts import render, redirect
from .models import Movie
from django.http import HttpResponse


def movie_listing(request):
    movies = Movie.objects.all()
    return render(request, 'movie/listing.html', {'movies': movies})

def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return render(request, 'movie/404.html')
    return render(request, 'movie/detail.html', {'movie': movie})

def movie_search(request):
    query = request.GET.get('q', '')
    results = Movie.objects.filter(title__icontains=query)
    return render(request, 'movie/search_results.html', {'results': results, 'query': query})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_listing')
    else:
        form = MovieForm()
    return render(request, 'movie/add_movie.html', {'form': form})

def toggle_favorite(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.is_favorite = not movie.is_favorite
    movie.save()
    return redirect('movie_listing')

def movie_category(request, category):
    if category == 'liked':
        movies = Movie.objects.order_by('-user_rating')[:5]
    elif category == 'newest':
        movies = Movie.objects.order_by('-release_date')[:5]
    elif category == 'genre':
        movies = Movie.objects.values('genre').distinct()
    return render(request, 'movie/category.html', {'movies': movies})


