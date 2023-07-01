from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # path('weapon_item/<int:weapon_item_id>/', views.weapon_item, name='weapon_item')
]
