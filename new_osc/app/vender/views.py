from django.shortcuts import render , redirect, HttpResponse
from django import views
from .models import Vender
from .forms import (
     VenderForm,
     LoginForm,
)
from app.product.models import Product

from django.contrib.auth import password_validation, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def VenderView(request):
    vender = VenderForm(request.POST)
    if vender.is_valid():
        vender.save()
    return render(request,'vender.html',context={'vender' : vender})



def about(request):
     return render(request,'about.html',{})
    
def contact(request):
     return render(request,'contact.html',{})

def index(request):
     return render(request,'index.html',{})

def mens(request):
     color = request.GET.get('color', None)
     if color != None:
          all_mans = Product.objects.filter( color = color )
    
     else:
          all_mans = Product.objects.filter(product_type = 'M')
     
     
     return render(
          request,
          'mens.html',
          {
               'all_man' : all_mans,
          })
    
def single(request, pid):

     product = Product.objects.get( id = pid )
     return render(
          request,
          'single.html',
          {
               'product' : product
          })

def womens(request):
     color = request.GET.get('color', None)
     if color != None:
          all_womans = Product.objects.filter( color = color )

     else:
          all_womans = Product.objects.filter(product_type = 'F')
     
     
     return render(
          request,
          'womens.html',
          {
               'all_woman' : all_womans,
          }
     )
    
