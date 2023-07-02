# import models
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import WeaponItem


def index(request):
    weapons_list = WeaponItem.objects.order_by("item_license")

    context = {"weapon_list": weapons_list}
    return render(request, "index.html", context)


def detail(request, item_id):
    weapon_item = get_object_or_404(WeaponItem, pk=item_id)
    return render(request, "detail.html", {"weapon_item": weapon_item})
