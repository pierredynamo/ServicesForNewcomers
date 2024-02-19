from django.shortcuts import render
from django.http import HttpResponse

"""
This is the home page of the project
"""
def home(request):
    return HttpResponse("<h1> Services for newcomers available soon ...  </h1>")
