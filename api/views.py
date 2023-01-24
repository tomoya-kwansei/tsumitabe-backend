import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets, permissions
from .models import *
from .serializers import UserSerializer

from django.middleware.csrf import get_token

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticated, )


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("認証されていないユーザです", status=401)
        return JsonResponse(UserSerializer(request.user).data, status=200)

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        user = authenticate(email=params["email"], password=params["password"])
        if user == None:
            return HttpResponse("正しいメールアドレスまたはパスワードを入力してください。", status=401)
        login(request, user)
        return HttpResponse("ログインに成功しました", status=200)


class CSRFTokenView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(get_token(request), status=200)
