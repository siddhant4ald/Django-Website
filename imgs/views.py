from django.shortcuts import render,redirect
from imgs.models import *

# Create your views here.
def imgs(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    data= {'images':images,'cats':cats}

    return render(request,"imgs.html",data)

def imgshow(request,cid):
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    
    

    images=Image.objects.filter(cat=category)
    data= {'images':images,'cats':cats}

    return render(request,"imgs.html",data)
    