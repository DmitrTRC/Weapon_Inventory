from django.urls import path
from . import views

app_name = 'Inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:weapon_id>/', views.detail, name='detail')
]
