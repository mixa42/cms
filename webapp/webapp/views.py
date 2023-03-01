from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu
import time


def goals_by_link(request, link):
    #return HttpResponse(f'The timeframe is {link}')
    active = Menu.objects.filter(url=link)
    if len(active) == 0:
        active = Menu.objects.filter(pk=int(link))
        
    return render(request, 'index.html', {'active_link':link, 'title': active[0].title, 'curtime': time.time()})

def index(request):
    link = Menu.objects.filter(parent_id=None)[0].url
    if link == None:
        link = Menu.objects.filter(parent_id=None)[0].pk
        active = Menu.objects.filter(pk=link)
    else:
        active = Menu.objects.filter(url=link)
        
    
    
    return render(request, 'index.html', {'active_link': link, 'title': active[0].title, 'curtime': time.time()})