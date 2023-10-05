from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from .forms import CustomUserCreationForm
#from django.middleware.csrf import _get_new_csrf_token
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token


def signup(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form':form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

def profile(request): 
    return render(request, 'profile.html')


def home(request):
    logout(request)  
    return render(request, 'home.html')

def homesignin(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'homesignin.html', {'form':form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'homesignin.html', {'form': form})
    
def dashboard(request):
    return render(request, 'dashbrd.html')

# def register_user(request):
#     context = {}
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = CustomUserCreationForm(auto_id=False)
#     context['form'] = form
#     return render_to_response('templates/signup.html',context)
#@_get_new_csrf_token
@csrf_exempt


def user_logout(request):
    requires_csrf_token
    logout(request)
    return render(request,'home.html')
    
def csrf_failure(request, reason=""):
    return render('403_csrf.html')

def index(request):
    logout(request)
    return render(request, 'index.html')

def lgn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/employee/dashboard/')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'index1.html', {'form':form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'index1.html', {'form': form})
    
def msbkg(request):
    return render(request, 'msbooking.html')