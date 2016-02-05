from django.conf.urls import url, include
#from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    url(r'^register/', views.CreateUserView.as_view(), name='user-register'),
    url(r'^api-token-auth/', views.GetAuthToken.as_view(), name='user-token'),
]

