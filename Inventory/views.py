# import models
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the Inventory index.")


def weapon_items(request):
    return HttpResponse("You're at the weapon items.")


def weapon_item(request, weapon_item_id):
    return HttpResponse("You're looking at weapon item %s." % weapon_item_id)
