from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('weapon_detail/<int:weapon_item_id>/', views.detail, name='detail')
]
