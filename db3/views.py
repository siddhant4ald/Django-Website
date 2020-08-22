from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import * 
from django.shortcuts import get_object_or_404



def index(request):
	return render(request,'index.html')

def insert (request):
	
	if request.POST:
		sobj = Student()
		sobj.sid=request.POST["t1"]
		sobj.sname=request.POST["t2"]
		sobj.semail=request.POST["t3"]
		sobj.scity=request.POST["t4"]
		sobj.sage=request.POST["t5"]
		sobj.save()
		info={'msg':'Inserted'}
		#return HttpResponse("Record Inserted")
		return render(request,'insert.html',info)
	else:
		return render(request,'insert.html')

def search(request):
	if request.POST:
		srch=request.POST['srh']

		if srch:
			match=Student.objects.filter(Q(sname__icontains=srch) | Q(sid__icontains=srch))
			if match:
				return render(request,'search.html',{'sr':match})
			else:
				messages.error(request,'Not found')
		else: 
			return HttpResponseRedirect('/search/')
	return render(request,'search.html')


def show(request):
	rs=	Student.objects.all()
	return render(request,'show.html',{'records':rs})

def delete(request):
	if request.method=="POST":
		gid=request.POST["t1"]
		rs=Student.objects.filter(sid=gid).delete()
		if rs[0]!=0:
			return render(request,'delete.html',{'info':'Record deleted'})
		else:
			return render (request,'delete.html',{'info':'Record not deleted'})
	else:
		return render(request,'delete.html')



def update(request):
	rs=	Student.objects.all()
	return render(request,'update.html',{'records':rs})






def updel(request):
	if request.method=="GET":
		gid=request.GET["sid"]
		rs=Student.objects.filter(sid=gid).delete()
		rs=	Student.objects.all()
		return render(request,'update.html',{'records':rs})

def edit(request):
	if request.method=="GET":
		gid=request.GET["sid"]
		rs=Student.objects.filter(sid=gid)
		return render(request,'edit.html',{'records':rs})

def updateres(request):
	if request.POST:
		gid=request.POST["t1"]
		sobj=Student.objects.get(sid=gid)
		sobj.sname=request.POST["t2"]
		sobj.sage=request.POST["t3"]
		sobj.semail=request.POST["t4"]
		sobj.scity=request.POST["t5"]
		sobj.save()
		rs=Student.objects.all()
		return render(request,'update.html',{'records':rs})

def about(request):
    return render(request,'about.html')

