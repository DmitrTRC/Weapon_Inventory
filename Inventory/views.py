from django.shortcuts import render


def index(request):
    return render(request, 'Inventory/index.html')


def weapon_items(request):
    return render(request, 'Inventory/weapon_items.html')


def weapon_item(request, weapon_item_id):
    return render(request, 'Inventory/weapon_item.html', {'weapon_item_id': weapon_item_id})
