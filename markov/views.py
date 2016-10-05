from django.shortcuts import render
from django.http import JsonResponse,Http404
from models import * 
from managers import *

def new_plot(request):
    
    text =  generate_random_text() 
    print(text)

    return JsonResponse({'text':text})

