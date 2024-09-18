from rest_framework import serializers
from .models import CategoriaServicio

class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        fields = ('id', 'nombre', 'descripcion', 'estado', 'createdAt')
        read_only_fields = ('createdAt', )