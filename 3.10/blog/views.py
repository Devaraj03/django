from blog.urls import *
from django.shortcuts import render

def indexes(request):
    return render(request,'index.html')