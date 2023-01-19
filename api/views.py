from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, permissions
from .models import *
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # TODO: のちに認証を必要とする設計へ変更
    # permission_classes = (permissions.IsAuthenticated, )
