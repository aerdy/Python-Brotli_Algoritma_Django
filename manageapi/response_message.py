__author__ = 'Jarod'
import json as simplejson

def response_404():
    data = simplejson.dumps({'code': '401',
                                 'message':
                                {
                                 'registeurl': 'http://kabisat.com/development',
                                 'result': 'Sistem Melakukan Register development Kabisat',
                                }
                            })
    return data

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