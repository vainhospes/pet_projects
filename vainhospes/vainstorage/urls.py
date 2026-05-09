from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from . import converters
from . import views

# register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('add_good/', views.add_good, name='add_good'),
    path('show_seasons/', views.show_seasons, name='show_seasons'),
    path('clothes/<slug:clothe_season>/', views.show_clothes, name='clothes'),
    path('product/<slug:product_slug>/', views.show_product, name='product'),
    path('tag/<slug:tag_slug>/', views.show_tag_clothes, name='tag'),
]
