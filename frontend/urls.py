from .views import home
from django.urls import include, path
from frontend import views

''' The function of this file is to define which view will be accessed by a user if 
    they access a certain URL. In this case, when they access the root URL, they will 
    be directed to the home view.'''
urlpatterns = [
    path( '',  home, name='home' ),
    path( 'testpage',  views.test, name='test' ),
    path( 'loginpage',  views.login, name='login' ),

]