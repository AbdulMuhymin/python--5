# from django.shortcuts import render
# from . models import place
#
#
# def demo(request):
#    # name="India"
#     obj = place.objects.all()
#
#     return render(request,"index.html",{'result':obj})
# # def addition(request):
# #    x=int(request.GET['num1'])
# #    y=int(request.GET['num2'])
# #    res=x+y
# #    return render(request,"About.html",{'result':res})

# from django.contrib.auth.models import User
# from django.shortcuts import render

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#
#     user = User.objects.create_user(username=username, password=password, last_name=last_name,
#                                     first_name=first_name, email=email)
#     user.save()
#     print("User created")
#
#     return render(request, "register.html")
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from testapp.models import place,person


def demo(request):
    obj = place.objects.all()
    obj2 = person.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2})


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, last_name=last_name,
                                                first_name=first_name, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
