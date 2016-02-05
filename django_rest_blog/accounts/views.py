from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import parsers, renderers

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class GetAuthToken(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer,)


