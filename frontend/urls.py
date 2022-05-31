from django.urls import path
from .views import home

''' The function of this file is to define which view will be accessed by a user if 
    they access a certain URL. In this case, when they access the root URL, they will 
    be directed to the home view.'''
urlpatterns = [
    path( '',  home, name='home' ),
    path( '/', home, name='home' ),
]