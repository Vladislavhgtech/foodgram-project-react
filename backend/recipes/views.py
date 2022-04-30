from .models import Recipe
from rest_framework import generics


class RecipeAPIView (generics.ListAPIView):
    queryset = Recipe.objects.all()
