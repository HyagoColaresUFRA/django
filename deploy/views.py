from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
     return HttpResponse("INDEX")

def update(request):
     os.system("git pull origin master")
     return HttpResponse("UPDATE")
