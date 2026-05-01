from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls home page.")

def clothes(request, season):
    return HttpResponse(f"<h1>{season}</h1>")

def product(request, product_id):
    return HttpResponse(f"<h1>ID Товара: {product_id}</h1>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив года: {year}</h1>")