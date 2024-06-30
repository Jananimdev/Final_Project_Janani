from django.shortcuts import render, get_object_or_404, redirect
from .models import details


def index(request):
    posts = details.objects.all()
    return render(request, 'index.html', {'posts': posts})
# Create your views here.



def dashboard(request):
    return render(request,'dashboard.html')