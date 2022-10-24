from quizzApp.models import Users

def get_top_users(request):

    #Request users from database ordered by number of correct answers
    top = Users.objects.order_by('nr_respostas_corretas').reverse().values('id','nr_respostas_corretas','nome')
    # print(top)
    top_ids = [user['id'] for user in top]

    #Get Top 10 LeaderBoard
    ret= { 'users': []}

    #Check if there are 10 users or more
    if len(top) < 10:
        for object in top:
            ret['users'].append( (object['nome'],object['nr_respostas_corretas']))

    else:
        #Iterete over the leaderboard top and save to a dictionary
        for indx_object in range(10):
            ret['users'].append( (top[indx_object]['nome'],top[indx_object]['nr_respostas_corretas']))


    #Get user place in the leaderboard
    if (id_us := request.user.id) != None:
        print(id_us)
        ret['user_place'] =  top_ids.index(id_us) + 1

    else:
        print("AUTH ERRORR!!!!!!")
        ret = "AUTH ERROR"

    ret['top1'] = ret['users'][0][0]
    ret['top2'] = ret['users'][1][0]
    ret['top3'] = ret['users'][2][0]

    return ret