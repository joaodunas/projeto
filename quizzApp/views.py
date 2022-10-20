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

        #if if user or email exists
        check_old_users = User.objects.values('username','email')
        user_list = []
        mail_list = []

        for i in check_old_users:
            user_list.append(i['username'])
            mail_list.append(i['email'])

        if e in user_list:
            raise Exception("Username already registered")

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




