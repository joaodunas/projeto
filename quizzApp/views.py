import json
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from quizzApp.models import Users
from quizzApp.api.serializers import UsersSerializer
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, template_name="index.html")



def halloffameView(request):
    return render(request, template_name="halloffame.html")


def loginView(request):
    return render(request, template_name="registration/login.html")


def registerView(request):
    return render(request, template_name="registration/register.html")
    
######


@api_view(['GET'])
def gen_users(request,num_users):
    
    if gen(num_users) == 0:
        return Response("Success")
    return Response("Error!")


@api_view(['GET'])
def get_all_users(request):
    allUsers = Users.objects.all()
    serializer =  UsersSerializer(allUsers, many = True)
    # ret= {}
    # for object in all:
    #     ret[object['id']] = object['nome']

    return Response(serializer.data)


#####

def get_random_string(length):
    import string,random

    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def gen(nr):
    from quizzApp.models import Users

    try:
    
        last_user_id = Users.objects.order_by('id').reverse().values('id')[0]['id'] + 1

        for i in range(last_user_id,last_user_id+nr):
            string_name = get_random_string(8)
            Users.objects.create(id=i,nome=string_name,email=f'{string_name}@gmail.com',nr_respostas_corretas = 0)
        

    except Exception as e:
        print(f'Error: {e}')
        return 1

    return 0




