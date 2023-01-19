import factory

from faker import Faker

from .models import *


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = Faker().email()
    password = Faker().word()
