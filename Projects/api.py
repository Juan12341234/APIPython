from .models import CategoriaServicio
from rest_framework import viewsets, permissions
from .serializers import CategoriaServicioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaServicio.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = CategoriaServicioSerializer