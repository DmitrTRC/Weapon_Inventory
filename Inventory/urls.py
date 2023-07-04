from django.urls import path
from .views import about_us, index

app_name = 'Inventory'

urlpatterns = [

    path('', index),
    path('about/', about_us),

]
