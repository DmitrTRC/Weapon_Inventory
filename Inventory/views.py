from django.shortcuts import render, HttpResponse


def about_us(request):
    return HttpResponse('Hello Inventory')


def index(request):
    return HttpResponse('Index page')
