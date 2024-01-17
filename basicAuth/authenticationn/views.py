from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

#auth models and func
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout  # Import logout explicitly

# Create your views here.

def home(request):
    return render(request, 'authenticationn/index.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    context = {'registerform': form}
    return render(request, 'authenticationn/register.html', context=context)

def login(request):
    form1 = LoginForm()
    if request.method == 'POST':
        form1 = LoginForm(request, data=request.POST)
        if form1.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)  # Fix the import here
                return redirect("dashboard")
    context = {'loginform': form1}
    return render(request, 'authenticationn/login.html', context=context)





def dashboard(request):
    return render(request, 'authenticationn/dashboard.html')
    
