from django.shortcuts import render
from portfolio.templates import portfolio

from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'portfolio/home.html', context )
        #HttpResponse('images\Mypic1.jpg')


def discover(request):
    context = {}
    return render(request, 'portfolio/discover.html', context )

