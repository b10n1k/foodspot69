from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, redirect, render

def main(request):
    return render(request,'main.html',{'view_title':"Menu",})

def profile(request):
    return render(request,'profile.html')

def order(request):
    return render(request,'order.html')

