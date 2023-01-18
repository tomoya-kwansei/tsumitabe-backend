from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, permissions
from .models import *
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
