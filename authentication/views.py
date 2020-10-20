from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def authlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Email or password invalid!')

    return render(request, 'login.html')


def authregistration(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['Confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.error(request, 'Username Already Exit ')
            elif User.objects.filter(email=email):
                messages.error(request, 'Email Already Exit ')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('profile')

        else:
            messages.error(request, 'Password and Confirm password not matched ')

    return render(request, 'registration.html')


def forgotpassword(request):
    return render(request, 'forgot.html')


def userlogout(request):
    logout(request)
    messages.success(request, 'Successfully logout!')
    return redirect('login')
