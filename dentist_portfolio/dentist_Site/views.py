import re
from django.shortcuts import render

def homePage(request):
    return render(request,'home.html',{})

def contactPage(request):
    if request. == 'post':
        do stuff
    else:   
        return render(request,'contact.html',{})
