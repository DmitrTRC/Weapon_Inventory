from django.shortcuts import render, HttpResponse

from .models import WeaponItem


def about_us(request):
    return HttpResponse('Hello Inventory')


def index(request):
    weapon_list = WeaponItem.objects.order_by('item_license')

    context = {
        'weapon_list': weapon_list
    }

    return render(request, 'index.html', context)
