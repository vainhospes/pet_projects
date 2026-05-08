from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import upper
from django.template.loader import render_to_string
from django.urls import reverse
from jedi.third_party.typeshed.stubs.pyasn1.pyasn1.type.tag import Tag

from vainstorage.models import Product, Season, TagProduct

# Create your views here.
menu = [{'title': 'О нас', 'url_name': 'about'},
        {'title': 'Добавить товар', 'url_name': 'add_good'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

db_clothes = [
    {
        'id': 1,
        'name': 'Футболка',
        'season': 'summer',
        'price': 100,
        'description': 'Базовая хлопковая футболка прямого кроя. Мягкий дышащий материал, круглый вырез, усиленные швы. Идеально подходит для повседневной носки и спорта. Доступна в белом, чёрном и сером цветах.'
    },
    {
        'id': 2,
        'name': 'Джинсы',
        'season': 'spring',
        'price': 200,
        'description': 'Удобные спортивные штаны из плотного трикотажа. Свободный крой, эластичный пояс на шнурке, два боковых и один задний карман. Не мнутся, быстро сохнут. Подходят для тренировок и отдыха.'
    },
    {
        'id': 3,
        'name': 'Куртка',
        'season': 'winter',
        'price': 300,
        'description': 'Лёгкая ветровка из водоотталкивающей ткани. Регулируемый капюшон, застёжка на молнию, два внутренних кармана. Дышащая подкладка из сетки. Компактно складывается в чехол. Отличный выбор для прохладной погоды.'
    },
]

db_seasons = [
    {'id': 1, 'name' : 'Зима', 'slug': 'winter'},
    {'id': 2, 'name' : 'Лето', 'slug': 'summer'},
    {'id': 3, 'name' : 'Весна', 'slug': 'spring'},
    {'id': 4, 'name' : 'Осень', 'slug': 'autumn'},
]

def home(request):
    # t =  render_to_string('vainstorage/home.html')
    # return HttpResponse(t)
    data = {
        'title' : 'Главная страница',
        'menu' : menu,
    }
    return render(request, 'vainstorage/home.html', data)

def about(request):
    data = {
        'menu': menu,
    }
    return render(request, 'vainstorage/about.html', data)

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
        "menu": menu,
        'clothes': clothes,
        'season': clothe_season,
    }
    return render(request, 'vainstorage/clothes.html', context = data)

def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    data_product = {
        'title': product.name,
        'menu': menu,
        'product': product,
    }

    return render(request, 'vainstorage/product.html', data_product)

def show_tag_clothes(request, tag_clothes):
    tag = get_object_or_404(TagProduct, slug=tag_clothes)
    clothes = tag.tags.filter(is_available=Product.available.AVAILABLE)
    data = {
        'title': tag.name,
        'menu': menu,
        'clothes': clothes,
    }

    return render(request, 'vainstorage/tag_clothes.html', context=data)

def archive(request, year):
    if year > 2026:
        url_redirect = reverse('clothes', args=('winter',))

        return redirect(url_redirect)

    return HttpResponse(f"<h1>Архив года: {year}</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")