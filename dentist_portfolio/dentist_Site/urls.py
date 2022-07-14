import imp
from django.urls import path
from . import views

urlpatterns =[
    path('',views.homePage,name="homePage"), 
    path('contact.html/',views.contactPage,name="contactPage"), 
]
