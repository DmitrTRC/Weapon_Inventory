# import models
from django.http import HttpResponse
from django.shortcuts import render

from .models import WeaponItem


def index(request):
    weapons_list = WeaponItem.objects.order_by("item_license")

    context = {"weapon_list": weapons_list}
    return render(request, "index.html", context)
