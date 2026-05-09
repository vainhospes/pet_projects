from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import upper
from django.template.loader import render_to_string
from django.urls import reverse

from vainstorage.models import Product, Season, TagProduct

# Create your views here.


def home(request):
    data = {
        'title' : 'Главная страница',
    }
    return render(request, 'vainstorage/home.html', data)

def about(request):
    return render(request, 'vainstorage/about.html')

def show_seasons(request):
    return render(request, 'vainstorage/show_seasons.html')

def add_good(request):
    return HttpResponse("Добавление товара")

def contact(request):
    return HttpResponse("Контакты")

def login(request):
    return HttpResponse("ВХОД В ЛОГИН")

def show_clothes(request, clothe_season):
    seasons = Season.objects.filter(slug__in=[clothe_season, 'all'] )
    clothes = Product.available.filter(season__in=seasons)

    data = {
        'title': "Одежда",
        'clothes': clothes,
        'season': clothe_season,
    }
    return render(request, 'vainstorage/clothes.html', context = data)

def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    data_product = {
        'title': product.name,
        'product': product,
    }

    return render(request, 'vainstorage/product.html', data_product)

def show_tag_clothes(request, tag_slug):
    tag = get_object_or_404(TagProduct, slug=tag_slug)
    clothes = tag.tags.filter(is_available=Product.Status.AVAILABLE)
    data = {
        'title': tag.name,
        'clothes': clothes,
    }

    return render(request, 'vainstorage/clothes.html', context=data)

def archive(request, year):
    if year > 2026:
        url_redirect = reverse('clothes', args=('winter',))

        return redirect(url_redirect)

    return HttpResponse(f"<h1>Архив года: {year}</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")