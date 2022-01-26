from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .models import Pizza
from .permissions import IsAuthorOrAuthOrReadOnly
from .serializers import PizzaSerializer, UserSerializer

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
