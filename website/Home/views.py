from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'location':'Katlehong',
        'category':'Food',
        'date': 'August 27, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':post
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html',{'title':'About'})
