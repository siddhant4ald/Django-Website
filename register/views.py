'''from django.shortcuts import render,redirect
#from django.contrib.auth import login,authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.http import HttpResponse
# Create your views here.
def register(response):
    if response.method=="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/index")
    else:
        form=RegisterForm()

    return render(response,'register/register.html',{"form": form})
'''



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm



def login(request):
    
    return redirect('login')

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register/register.html', {'form': f})