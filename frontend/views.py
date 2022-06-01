from asyncio.windows_events import NULL
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world from Django")

# Read/chosen from csv fil ex. 
def items(request):
    return NULL

# Item specific item i units
def itemSingle(request):
    return NULL

# Scanner input - manual handscanner
def scanning(request):
    return NULL

# DB field location handling
def itemLocation(request):
    return NULL
