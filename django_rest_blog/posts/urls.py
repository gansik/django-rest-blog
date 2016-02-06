from rest_framework import routers

from .views import PostsViewSet

router = routers.SimpleRouter()
router.register(r'post', PostsViewSet)
urlpatterns = router.urls
