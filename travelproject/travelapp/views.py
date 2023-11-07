from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Guide

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objj=Guide.objects.all()
    # name="india"
    return render(request,"index.html",{'result':obj,'results':objj})

# def about(request):
#     return render(request,"about.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})