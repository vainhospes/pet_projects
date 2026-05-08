from django import template
from vainstorage import views
from vainstorage.models import TagProduct, Season

register = template.Library()

@register.inclusion_tag('vainstorage/list_seasons.html')
def header_show_seasons():
    seasons = Season.objects.all()
    return {'seasons': seasons}

@register.inclusion_tag('vainstorage/list_tags.html')
def show_all_tags():
    return {'tags': TagProduct.objects.all()}