from django.db import models

# Create your models here.
class CategoriaServicio(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=False)
    estado = models.BooleanField(default=True, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)