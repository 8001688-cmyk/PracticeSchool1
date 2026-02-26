import http
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

def index(request):
    now = datetime.now()

    return render(
        request,
        "MyApp1/index.html", 
        {
            'title' : "Django Home",
            'message' : "Hello Django!",
            'content' : "on" + now.strftime("%A, %d %B, %Y at %X")
        }

    )

