from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    # user has info and wants to create an account now
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2'] and request.POST['username']!='':
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
               user =  User.objects.create_user(username= request.POST['username'],password= request.POST['password1'])
               auth.login(request,user)
               return redirect('home')
        else:
            if request.POST['username']=='':
                return render(request,'signup.html',{'error':'Please, fill the Form'})
            else:
                return render(request,'signup.html',{'error':'passwords must match'})


    else:
        #user wants to enter some data

        return render(request,'signup.html')

def login(request):
    method = request.method
    if request.method == 'POST':
        print("login post method")
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            print("login user is authenticated")
            auth.login(request,user)
            return redirect('home')
        else:
            print("login user is not authenticated")
            return render(request,'login.html',{'error':'the username or passowrd is incorrect','method':{method}})

    else:
         return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        print("logout: method==post")
        auth.logout(request)
        return redirect('home')
