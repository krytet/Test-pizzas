from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PeopleViewSet, PizzaViewSet, UserViewSet

router = DefaultRouter()
router.register('restaurants', UserViewSet, 'restaurants')
router.register('pizzas', PizzaViewSet, 'pizzas')
router.register('people', PeopleViewSet, 'people')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
