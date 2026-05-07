from django import template
from vainstorage import views

register = template.Library()

@register.simple_tag()
def get_seasons():
    return views.db_seasons

@register.inclusion_tag('vainstorage/list_seasons.html')
def header_show_seasons():
    seasons = views.db_seasons
    return {'seasons': seasons}