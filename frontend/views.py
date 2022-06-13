from asyncio.windows_events import NULL
from collections import namedtuple
from http.client import BAD_REQUEST
from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponse
#from django.views.decorators.csrf import csrf_protect
#from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from backend.AuthLogin import loginMethod
from backend.DBConnections import CreateUser
from rest_framework.decorators import api_view
import bcrypt

from backend.models import LoginAuthModel

# Create your views here.
def home(request):
    return HttpResponse("Hello world from Django")

# Read/chosen from csv fil ex. 
def items(request):
    return NULL

# Item specific item i units
def itemSingle(request):
    return NULL

def itemNew(request):
    return NULL

# Scanner input - manual handscanner
def scanning(request):
    return NULL

# DB field location handling
def itemLocation(request):
    return NULL

def test(request):
    if request.method == 'POST':
        return HttpResponse("Yes")
    else: 
        return HttpResponse("This is a POST only Endpoint")

#TODO
#use exisitng log into serverdesk_sager which utilizes "barcodes" / other unique aspects for a log search.
#currently theres only tracking of ordre numbers, but needs a unique attribute for each item

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
      #  print(f"data {request.data}")        
        username = request.data.get('username', 0)
        password = request.data.get('password', 0)
        if not username or not password :
            return HttpResponseBadRequest()
       # CreateUser(username, password, "Test")
        

#        loginObj = namedtuple("ObjectName", request.data.keys())(*request.data.values())
#        print(loginObj.password)

        return HttpResponse(f"{loginMethod(password, username)}")
    else: 
        return HttpResponse("This is a POST only Endpoint")