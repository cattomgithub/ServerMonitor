from django.shortcuts import render

def index (req):
    context = {}
    return render(req, 'index.html', context)