from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from quizzApp.models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import json
from django.contrib.auth import authenticate



@api_view(['POST'])
@permission_classes([AllowAny]) 
def loginUser(request):
    
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    e = body['username']
    p = body['password']
    
    user = authenticate(username = e, password = p)
    login(request, user)
    
    
    if user is not None:
    # A backend authenticated the credentials
        
        return Response({"autenticado": "true"})
    else:
     #No backend authenticated the credentials
      
        return Response({"autenticado": "false"})


@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    e = body['username']
    p = body['password']
    g = body['email']

    try: 

        #if if email already exists
        check_old_users = User.objects.values('email')
        mail_list = []

        for i in check_old_users:
            mail_list.append(i['email'])

        if e in mail_list:
            raise Exception("Mail already exists")


        user = User.objects.create_user(e, g, p)
        users = Users.objects.create(id=user.id,nome=e,email=g,nr_respostas_corretas = 0)
        user.save()
        users.save()

    except Exception as e:
        print(e)
        return Response({"autenticado": "false"})


    return  Response({"autenticado": "true"})