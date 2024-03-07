from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def hello_view(request):
    return render(request, "integration/hello.html")

def models(request):
        items = MyModel.objects.all()
        return render(request, 'integration/models.html',  {"models": items} )