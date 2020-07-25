from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def home(request):
    #return HttpResponse("HIdj")
    return render(request, 'covid/home.html')

def covid(request):
    return render(request, 'covid/covid.html')

def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username=loginusername, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('patients')
        else:
            messages.success(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'covid/html/login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmPassword']
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.save()
        messages.success(request, "Your Account has been successfully created. Login to Continue")
        return redirect('login')
    return render(request, 'covid/html/register.html')

def Patients(request):
    if request.POST:
        patient_name = request.POST['patientname']
        covidtest = request.POST['exampleRadios']
        return redirecr('patient')
    params = {'nothing':1}
    return render(request, 'covid/html/patients.html', params)

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('homepage')
# Create your views here.
