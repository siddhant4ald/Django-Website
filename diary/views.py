from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def diary(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'diary.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/diary')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'add.html', context)
def deldiary(request):
	if request.method=="GET":
		gid=request.GET["text"]
		rs=Entry.objects.filter(text=gid).delete()
		rs=	Entry.objects.all()
		return redirect('/diary')
