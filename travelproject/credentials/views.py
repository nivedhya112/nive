from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken.')
                return redirect('register')
            else:
                # Use create method for custom fields
                user = User.objects.create(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password,
                )
                # Set password using set_password method
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
