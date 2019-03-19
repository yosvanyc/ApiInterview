from django.http import JsonResponse
import pdb, json

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Receta
from .serializers import RecetaSerializer


class RecetaList(generics.ListAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer


class RecetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer


class RecetaCreate(generics.CreateAPIView):
    serializer_class = RecetaSerializer


def recipeByUser(request, pk):
    recetas = Receta.objects.filter(user_id=pk)
    data = []
    for r in recetas:
       data.append({
            'pk': r.pk,
            'name': r.name
        })
    return JsonResponse(data, safe=False)
