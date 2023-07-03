from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Inventory.urls')),  # Path '' put first
    path('admin/', admin.site.urls),
]
