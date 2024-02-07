from django.shortcuts import render,HttpResponse,redirect
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from .models import Headline

# Create your views here.

def index(request):
    context={}
    return render(request,'onionapp/index.html',context)
