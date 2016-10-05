from django.shortcuts import render
from django.http import HttpResponse,Http404
from models import * 
from managers import *
import json

def new_plot(request):
    if request.method == 'GET':

        text =  generate_random_text() 
        data  = text
    
        return HttpResponse(data,content_type="application/json")
    else:
        return HttpResponse("Bro wrong request type.")
