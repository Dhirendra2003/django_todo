# from django.http import HttpResponse
from django.shortcuts import render

def home(req):
  # return HttpResponse('<h1>Home page</h1>')
  return render(req ,'home.html')