from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import upper
from django.template.loader import render_to_string
from django.urls import reverse


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

def clothes(request, season):
    data = {
        'title': "Одежда",
        "menu": menu,
        'clothes': db_clothes,
        'season': season,
    }
    return render(request, 'vainstorage/clothes.html', context = data)

def product(request, product_slug, product_id):
    data_product = {'product_slug': upper(product_slug), 'product_id': product_id, 'colours': ['red', 'green', 'blue']}
    return render(request, 'vainstorage/product.html', data_product)

def archive(request, year):
    if year > 2026:
        url_redirect = reverse('clothes', args=('winter',))

        return redirect(url_redirect)

    return HttpResponse(f"<h1>Архив года: {year}</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")