from django.shortcuts import render
from django.http import JsonResponse,Http404
from models import * 
from managers import *
import json

def new_plot(request):
    
    text =  generate_random_text() 
    data = {'text':text}
    
    return JsonResponse(data,content_type="application/json")

