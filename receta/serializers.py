from rest_framework import serializers
from . import models


class RecetaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'user_id')
        model = models.Receta
