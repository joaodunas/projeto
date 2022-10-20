from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from quizzApp.models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import json
from django.contrib.auth import authenticate

@api_view(['GET'])
def get_top_users(request):


    if request.user.is_authenticated:
        #Request users from database ordered by number of correct answers
        top = Users.objects.order_by('nr_respostas_corretas').reverse().values('id','nr_respostas_corretas','nome')
        top_ids = [user['id'] for user in top]

        #Get Top 10 LeaderBoard
        ret= {}

        #Check if there are 10 users or more
        if (l := len(top)) < 10:
            for object,place in zip(top,range(1,l+1)):
                ret[place] = ret[place] = { "nr_respostas_corretas": object['nr_respostas_corretas'], "nome": object['nome']}

        else:
            #Iterete over the leaderboard top and save to a dictionary
            for object,place in zip(top,range(1,11)):
                ret[place] = { "nr_respostas_corretas": object['nr_respostas_corretas'], "nome": object['nome']}


        #Get user place in the leaderboard
        if (id_us := request.user.id) != None:
            print(id_us)
            ret['user_place'] =  { "nr_respostas_corretas": object['nr_respostas_corretas'], "nome": request.user.username, 'place': top_ids.index(id_us) + 1}

        else:
            print("AUTH ERRORR!!!!!!")

        response = Response(ret)

    #USER NOT LOGGED IN, REDIRECT
    else:
        response = Response("AUTH ERROR")
        print("not login")

    return response

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