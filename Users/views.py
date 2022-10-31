from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.

def IndexView(request):
    if not request.user.is_authenticated:
        return redirect('users/login ')
    else:
        user = request.user
        print("they're authenticated")
        template = loader.get_template('users/index.html')
        context = {'username': user.username}
        return HttpResponse(template.render(context,request))

def Register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print( "Account was successfully for " + user +"!")
            return HttpResponseRedirect('/users/profile/')
        else:
            print("invalid try again")
            return HttpResponseRedirect('/users/login/')

    context={'form':form}
    return render(request, 'users/register.html',context)



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None: #if they are an actual user
            login(request,user)
            print("SUCCESFFUL LOGIN FOR " + str(user) +"!")
            return HttpResponseRedirect('/users/profile/')
        else:
            print("bad bad bad bad ")
            messages.success(request,("There Was An Error in Logging In. Please Try Again."))
            return redirect('/users/login')
    if request.method == 'GET':
        print("this is a get request")


    context = {}
    return render(request,'users/login.html',context)
    # user = (authenticate(request,username=username,password=password))
    # if user is not None:
    #     login(request,user)
    #     #redirect to a success page
    #     return HttpResponseRedirect('/profile/')
    #
    # else:
    #     #return a error message
    #     print("invalid try again")
    #     return HttpResponseRedirect('/users/register')
    #     print('redirected back to register')

def Logout(request):
    logout(request)
    return render(request, 'users/logout.html',context={})


