from django.contrib import admin
from django.urls import path, include, re_path, register_converter
from . import converters
from . import views

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/<slug:season>/', views.clothes, name='clothes'),
    path('product/<int:product_id>/', views.product, name='product'),
    path("archive/<int:year>/", views.archive, name='archive'),
]
