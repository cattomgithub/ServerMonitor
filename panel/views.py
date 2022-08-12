from django.shortcuts import render
from django.template import loader
from .models import Server

def index(request):
    server_list = Server.objects.order_by('server_name')
    context = {
        'app_name': "Cat Tom's Server Monitor",
        'server_list': server_list,
    }
    return render(request,'index.html',context)
