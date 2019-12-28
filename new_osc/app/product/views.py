from django.shortcuts import render , redirect, HttpResponse
from django import views
from .models import Product
from .forms import ProductForm

# Create your views here.
def ProductView(request):
    product = ProductForm(request.POST)
    if product.is_valid():
        product.save()
    return render(request,'product.html',context={'product' : product})