from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    cache_key = f"recipe_{recipe_id}"  # unique cache key for each recipe
    recipe = cache.get(cache_key)

    if recipe is None:
        print("hit the db")
        recipe = get_object_or_404(Recipe, id=recipe_id)
        cache.set(cache_key, recipe, timeout=60*5)  # cache for 5 minutes
    else:
        print("hit the cache")

    return render(request, "recipe_detail.html", {"recipe": recipe})


    
