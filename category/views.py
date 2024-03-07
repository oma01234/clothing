from django.shortcuts import render, redirect
from django.contrib import messages
from category.models import Category
from sub_cat.models import SubCat

# Create your views here.


def create_category(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        b = Category(name=name)
        b.save()
        return redirect('category_list')

    return render(request, 'create_cat.html')


def category_list(request):

    cat = Category.objects.all()
    subcat = SubCat.objects.all()

    for sub_cat in subcat:
        for category in cat:
            if sub_cat.catid == category.pk:
                category.no_of_sub += 1
                num = category.no_of_sub
                print(category.name, num)
                print(sub_cat.item_name)

    return render(request, 'cat_list.html', {'cat': cat})
