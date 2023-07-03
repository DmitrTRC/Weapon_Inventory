from django.urls import path
from .views import about_us, index

urlpatterns = [

    path('', index),
    path('about/', about_us),

]
