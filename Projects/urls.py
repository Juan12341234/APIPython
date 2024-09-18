from rest_framework import routers
from .api import CategoriaViewSet

router = routers.DefaultRouter()

router.register('api/categoriaServicios', CategoriaViewSet, 'categorias')

urlpatterns = router.urls