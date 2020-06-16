from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('signin',views.logiN,name='logiN'),
]
