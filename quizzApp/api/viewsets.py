from rest_framework import viewsets
from quizzApp.api import serializers
from  quizzApp import models


class UsersViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.UsersSerializer
    queryset = models.Users.objects.all

    
