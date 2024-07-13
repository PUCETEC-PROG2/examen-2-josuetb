from django.http import HttpResponse
from django.template import loader
from .models import movies

def index(request):
    pokemons = movies.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movie}, request))

def movies(request, movies_id):
    movie = movies.objects.get(pk = movies_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))
