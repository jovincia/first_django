from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>Hello World!!!</h1>")


def about(request):
    return HttpResponse("<h1>About Us !!!</h1> <p> I will build an amazing website in Django. </p>")

def listings(request):
    return HttpResponse("<h1>Listings !!!</h1> <p> Here is all our listings. </p>")

def contacts(request):
    return HttpResponse("<h1>Contact Us !!!</h1> <p> Here you can contact us. </p>")

