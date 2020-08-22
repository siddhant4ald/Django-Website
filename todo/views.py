from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def index1(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(index1)


	context = {'tasks':tasks, 'form':form}
	return render(request, 'index1.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect(index1)

	context = {'form':form}

	return render(request, 'updateTask.html', context)
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect(index1)

	context = {'item':item}
	return render(request, 'deleteTask.html', context)



'''from django.shortcuts import render,redirect
from .models import todo
import requests

# Create your views here.
def note(request):
	data=todo.objects.all()
	return render(request,'note.html',{'data':data})

def add(request):
	tododata=request.POST['todo']
	todo_item=todo(content=tododata)
	todo_item.save()
	return redirect(note)

def deleteItem(request,todo_id):
	item = todo.objects.get(id=todo_id)
	item.delete()
	return redirect(note)
	'''