from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html',{'title':'About'})

def view_products(request):
    return render(request, 'home/view-products.html')
