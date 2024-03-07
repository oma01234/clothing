from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from . models import Item
from sub_cat.models import SubCat


def item_detail(request, position):

    subcat = SubCat.objects.filter(item_name=position)
    desired_value = request.GET.get('desired_value', '')
    if desired_value:
        # print(desired_value)
        request.session['name'] = desired_value
        title1 = dict(request.session.items())
        title2 = title1.get('name', '')
        print(title2)

    return render(request, 'item_detail.html', {'subcat': subcat})


def buy_now_check_out(request):

    name = request.session.get('name', [])
    if name == None:
        print('Expired')
    print(name, 'heett')
    names = Item.objects.all()

    return render(request, 'buy_now_check_out.html', {'name': str(name), 'names': names})


def add_to_cart(request, position):

    item = SubCat.objects.get(item_name=position)
    new_item = Item(name=item.item_name, price=item.item_price, pic=item.item_pic, pic_name=item.pic_name)
    new_item.save()

    cart_name = SubCat.objects.get(item_name=position).item_name

    return redirect('item_detail', position=cart_name)
    # set this path to go to the initial item detail after the main page


def cart(request):

    item_content = Item.objects.all()

    return render(request, 'cart.html', {'item_content': item_content})


def check_out(request):

    return render(request, 'check_out.html')


def item_delete(request, pk):

    item = Item.objects.get(pk=pk)

    fs = FileSystemStorage()
    fs.delete(item.pic_name)

    item.delete()

    return redirect('cart')
