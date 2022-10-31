from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

# Create your views here.

def IndexView(request):

    context = {}
    return render(request, 'register.html',context)
