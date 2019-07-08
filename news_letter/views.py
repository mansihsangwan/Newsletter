from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import Http404,HttpResponseRedirect, \
                        HttpResponse, HttpResponseForbidden
from django.urls import reverse
from .forms import *

def news_letter(request):


    context = {
        
    }
    return render(request, 'index.html', context)