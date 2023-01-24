from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *
from rest_framework.authtoken import views as auth_views


defaultRouter = routers.DefaultRouter()

defaultRouter.register('users', UserViewSet)

urlpatterns = []
urlpatterns += defaultRouter.urls

urlpatterns += path(r'login/', LoginView.as_view(), name="login"),
urlpatterns += path(r'csrftoken/', CSRFTokenView.as_view(), name="csrftoken"),
urlpatterns += path(r'api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
