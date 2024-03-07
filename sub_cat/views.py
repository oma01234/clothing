from django.shortcuts import render, redirect
from category.models import Category
from django.contrib import messages
from .models import SubCat
from django.core.files.storage import FileSystemStorage

# Create your views here.


def create_subcat(request):

    cat = Category.objects.all()

    if request.method == 'POST':

        Category_name = request.POST.get('CatName')
        get_cat_name = Category.objects.get(pk=Category_name).name
        get_cat_pk = Category.objects.get(pk=Category_name).pk

        item_name = request.POST.get('SubCatName')
        price = request.POST.get('price')

        if len(SubCat.objects.filter(item_name=item_name)) != 0:
            messages.error(request, "Name already chosen for another Sub Category")
            return redirect('create_subcat')

        else:
            try:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                pic = fs.url(filename)

                if str(myfile.content_type).startswith('image'):

                    if myfile.size < 9000000:

                        b = SubCat(item_name=item_name, item_price=price, item_pic=pic, catid=get_cat_pk, pic_name=filename)
                        b.save()
                        return redirect('subcat_list')

                    else:
                        fs = FileSystemStorage()
                        fs.delete(myfile)

                        messages.error(request, "Your file is bigger than 9mb")
                        return redirect('create_subcat')

                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    messages.error(request, "Your file is not a supported file type")
                    return redirect('create_subcat')

            except ValueError:
                messages.error(request, "Couldn't upload picture")
                return redirect('create_subcat')

    return render(request, 'create_subcat.html', {'cat': cat})


def subcat_list(request):

    sub_cat = SubCat.objects.all()

    return render(request, 'subcat_list.html', {'sub_cat': sub_cat})
