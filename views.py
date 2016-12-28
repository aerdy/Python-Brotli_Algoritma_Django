from django.shortcuts import render
from django.http import HttpResponse
from Test1 import models
import json as simplejson
from manageapi import response_message
from manageapi import manage_api
from django.views.decorators.csrf import csrf_exempt
import brotli

@csrf_exempt
def BrotliTest(request):
    imageupload = request.FILES.get('image')
    dataimage = brotli.compress(imageupload, quality=11, lgwin=22, lgblock=0, dictionary='')
        
    reg = models.Question.objects.create(image=dataimage)
    reg.save()
    data = response_message.responsesuccsess()
    return HttpResponse(data, content_type='application/json')

		