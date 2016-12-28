__author__ = 'Jarod'
from Test1 import models
def checktoken(token):
    try:
        viewdata = models.User_Developent.objects.get(tokenid=token)
        viewdata = True
    except:
        viewdata = False
    return viewdata

def responsesuccsess():
    data = simplejson.dumps({'code': '200',
                                 'message':
                                 {
                                 'result': 'ok',
                                 }
                            })
    return data

def responseerror(message):
    data = simplejson.dumps({'code': '400',
                                 'message':
                                {'message': message,
                                 'result': 'error',
                                }
                            })
    return data

