from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from category.models import Category
from sub_cat.models import SubCat
from barcode.models import Barcode
# Create your views here.

@csrf_exempt
def index(request):

    cat = Category.objects.all()
    subcat = SubCat.objects.all()

    latest_items = SubCat.objects.all().order_by('-pk')

    return render(request, 'index.html', {'cat': cat, 'subcat': subcat, 'latest': latest_items})


def mylogin(request):

    return render(request, 'login.html')


def myregister(request):

    return render(request, 'register.html')


def panel(request):

    return render(request, 'admin.html')
