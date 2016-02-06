from django.contrib.auth import get_user_model

from rest_framework import permissions, renderers
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class GetAuthToken(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer,)


class ProfileUserView(RetrieveAPIView):

    model = get_user_model()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    search_fields = ('title', 'body')

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()

    """
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'token': unicode(request.auth),  # None
        }
        return Response(content)

    """
