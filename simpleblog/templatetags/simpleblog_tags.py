from django.template import Library
from django.contrib.flatpages.models import FlatPage

from simpleblog.models import Category,Article

register = Library()

@register.inclusion_tag('tags/flatpage.html')
def flatpage():
    flatpages = FlatPage.objects.all()
    return {'flatpages':flatpages}

@register.inclusion_tag('tags/category.html')
def category():
    categorys = Category.objects.all()
    return {'categorys':categorys}
    
'''
@register.inclusion_tag('tags/latest.html')
def lastest():
    articles = Article.objects.order_by('-publish_at')[0:5]
    return {'articles':articles}
'''

@register.inclusion_tag('tags/archives.html')
def archives():
    dates = Article.objects.all().dates('publish_at','month',order='DESC')
    return {'dates':dates}
    
@register.inclusion_tag('tags/hots.html')
def hots():
    articles = Article.objects.order_by('-num_views')[0:5]
    return {'articles':articles}
