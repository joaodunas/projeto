from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quizzApp.models import Users
from quizzApp.api.serializers import UsersSerializer
from quizzApp.funcs import *
# Create your views here.

def index(request):
    return render(request, template_name="index.html")


def halloffameView(request):

    if request.user.is_authenticated:

        #Function that returns a dictionary with the top 10 users and the logged user place
        top_users = get_top_users(request)

        return render(request, template_name="halloffame.html",context = top_users)
    else:
        return render(request, template_name="registration/login.html")

def loginView(request):
    
    if request.user.is_authenticated:
        return halloffameView(request)
    else:
        return render(request, template_name="registration/login.html")


def registerView(request):
    if request.user.is_authenticated:
        return render(request, template_name="halloffame.html")
    else:
        return render(request, template_name="registration/register.html")
    
######
