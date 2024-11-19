from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     return HttpResponse("INDEX")

def update(request):
     os.system("git pull origin main")
     return HttpResponse("UPDATE")
