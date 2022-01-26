from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PizzaViewSet, UserViewSet


router = DefaultRouter()
router.register('restaurants', UserViewSet, 'restaurants')
router.register('pizzas', PizzaViewSet, 'pizzas')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
