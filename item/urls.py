from django.urls import path
from rest_framework import routers
from .api import ItemViewSet, CategoryViewSet, OrderViewSet, ReviewViewSet

# Define el enrutador
router = routers.DefaultRouter()
router.register("api/items", ItemViewSet, "items")
router.register("api/categorias", CategoryViewSet, "categorias")
router.register("api/reviews", ReviewViewSet, "reviews")
router.register("api/order", OrderViewSet, "order")

# Añade la URL para cargar imágenes
urlpatterns = router.urls