from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import views

from users import serializer
from users.models import User
from users.permissions import IsOwner
from users.serializer import RegistrationSerializer, ClientModelSerializer, MerchantModelSerializer


# Create your views here.

class RegistrationModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LoginView(views.TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializer.LoginSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = User.objects.filter(person=User.personality.CLIENT)
    serializer_class = ClientModelSerializer
    # permission_classes = (IsAdminUserOrReadOnly,)


class MerchantModelViewSet(ModelViewSet):
    queryset = User.objects.filter(person=User.personality.MERCHANT)
    serializer_class = MerchantModelSerializer
    permission_classes = (IsAuthenticated, IsOwner)
