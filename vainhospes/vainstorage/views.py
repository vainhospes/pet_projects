from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls home page.")

def clothes(request, season):
    print(request.POST)
    return HttpResponse(f"<h1>{season}</h1>")

def product(request, product_id):
    return HttpResponse(f"<h1>ID Товара: {product_id}</h1>")

def archive(request, year):
    if year > 2026:
        raise Http404()

    return HttpResponse(f"<h1>Архив года: {year}</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")