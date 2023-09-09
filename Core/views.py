from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from .models import Movie, Tag
from django.db.models import Count
import random

class ShowTags(View):
    def get(self, request, id=1, *args, **kwargs):
        movies = Movie.objects.filter(tags__id=id).annotate(dcount=Count('uuid'))
        tag = Tag.objects.filter(id=id)
        return render(request, 'movieList.html',
                      {'movies' : [
                         {"video" : movies  , "customTitle": "Tag : " + tag[0].title}
                      ]})

class ShowMovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        movie = Movie.objects.get(uuid=movie_id)
        tag = Tag.objects.all()
        return render(request, 'movieDetail.html', {
            'movie': movie,
            'tag': tag
        })

class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        movie = Movie.objects.get(uuid=movie_id)

        movie.save()
        movie = movie.file

        return render(request, 'showMovie.html', {
            'movie': movie
        })

class HomeMain(View):

    def get(self, request, *args, **kwargs):

        Bestmovies = Movie.objects.all().order_by('-views')
        listOfTags = list(Tag.objects.all().order_by('-priority'))

        return render(request, 'movieList.html', {
            'movies' : [
                {"video": Bestmovies , "customTitle":"Wybrane modele" },

            ], "listOfTags": listOfTags
        })


class Search(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        listOfTags = [x.title for x in Tag.objects.filter(title__icontains=query)]
        moviearr = {}
        movies = Movie.objects.filter(tags__title__icontains=query).order_by('-created').annotate(dcount=Count('uuid'))

        for mov in list(movies):
            for tag in mov.tags.all():
                if(tag.title in listOfTags):
                    try:
                      moviearr[str(tag.title)]
                    except:
                        moviearr[str(tag.title)] = []

                    moviearr[str(tag.title)].append(mov)

        allMovie = []
        for mov in listOfTags:
            try:
                moviearr[mov]
                allMovie.append({"video": moviearr[mov], "customTitle": "Tag: " + mov})
            except:
                print("Nie ma słuchawek z tym tagiem")
        if(len(listOfTags) == 0):
            print("Nie ma takiego tagu")

        movies2 = Movie.objects.filter(description__icontains=query).order_by('-created').annotate(dcount=Count('uuid'))

        movierest = Movie.objects.filter(tags__title__icontains="").exclude(tags__title__icontains=query).annotate(dcount=Count('uuid'))
        allMovie.append({"video": movies2, "customTitle": "Specyfikajca"})

        allMovie.append({"video": movierest, "customTitle": "Inne"})

        return render(request, 'movieList.html', {
            'movies' : allMovie,
        })
