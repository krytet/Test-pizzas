from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import People, Pizza
from .permissions import IsAuthorOrAuthOrReadOnly
from .serializers import PeopleSerializer, PizzaSerializer, UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAuthorOrAuthOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user)


class PeopleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'iin'
