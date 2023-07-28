from django.contrib.auth.models import User
from django.shortcuts import redirect, render , redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def About(request):
    return render(request,'about.html' )

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Logout(request):
    return render(request, 'base.html')

def Index(request):
    if not request.user.is_staff:
        return redirect ('login')
    return render(request, 'base.html')

def Login(request):
    error = ""
    if request.method =="POST":
        u = request.POST['adminName']
        p = request.POST['password']
        user = authenticate(username= u, password=p)
        try:
            if user.is_staff:
                Login(request,user)
                error = "no"

            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')
                