from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.
def IndexView(request):
    context = {}
    return render(request, 'homepage/homepage.html',context)
