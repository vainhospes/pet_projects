from django import template
from vainstorage.models import TagProduct, Season

register = template.Library()

@register.inclusion_tag('vainstorage/list_seasons.html')
def header_show_seasons():
    return {'seasons': Season.objects.all()}

@register.inclusion_tag('vainstorage/list_tags.html')
def show_all_tags():
    return {'tags': TagProduct.objects.all()}