from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout

# -----------------------
# LOGIN VIEW
# -----------------------
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # After login go to home page
        else:
           return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')



# -----------------------
# REGISTER VIEW
# -----------------------
def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # create user
        User.objects.create_user(username=username, password=password)

        return redirect('login')  # After register go to login

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('login')


# -----------------------
# HOME PAGE
# -----------------------
def home_page(request):
    return render(request, 'home.html')



# Create your views here.
