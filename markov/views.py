from django.shortcuts import render
from django.http import HttpResponse,Http404
from models import * 
from managers import *

def new_plot(request):
    twmgr = TripleToWordManager()
    stmgr = StartTripleManager()
    stgen = stmgr.new_start_triple()
    
    start_triple = stgen.next()
    print start_triple
    
    return HttpResponse(start_triple)

