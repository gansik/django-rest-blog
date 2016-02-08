from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
#from django.utils.decorators import method_decorator

from rest_framework import viewsets, permissions
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import filters

from .serializers import PostSerializer
from .models import Post



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class PostsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', )
    search_fields = ('title', 'bodytext')

    #@method_decorator(login_required)
    @list_route()
    def my(self, request):
        if not request.user.is_authenticated():
             raise PermissionDenied()

        posts = Post.objects.filter(owner=request.user)

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data)


    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        instance.slug = slugify(instance.title)
        serializer.save(owner=self.request.user)
