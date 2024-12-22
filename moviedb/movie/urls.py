"""
URL configuration for moviedb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls'),
    path('', views.movie_listing, name='movie_listing'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('search/', views.movie_search, name='movie_search'),
    path('add/', views.add_movie, name='add_movie'),
    path("accounts/", include("django.contrib.auth.urls"),
    path('toggle_favorite/<int:movie_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('category/<str:category>/', views.movie_category, name='movie_category'))),
]
