from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *

defaultRouter = routers.DefaultRouter()

defaultRouter.register('users', UserViewSet)

urlpatterns = []
urlpatterns += defaultRouter.urls

urlpatterns += path(r'login/', LoginView.as_view(), name="login"),
urlpatterns += path(r'csrftoken/', CSRFTokenView.as_view(), name="csrftoken"),
