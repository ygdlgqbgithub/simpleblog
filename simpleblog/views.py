from django.shortcuts import get_object_or_404,render
from datetime import datetime

from taggit.models import Tag

from simpleblog.models import Article,Category


def index(request,tag_name=None,category_id=None,year=None,month=None,
          template_name='simpleblog/index.html'):

    articles = Article.objects.filter(status=1)
    ctx = {}

    if tag_name:
        ctx['tag'] = get_object_or_404(Tag,name=tag_name)
        articles = articles.filter(tags__name=tag_name)

    if category_id:
        ctx['category'] = get_object_or_404(Category,id=category_id)
        articles        = articles.filter(category__id=category_id)

    if year and month:
        ctx['date'] = datetime(year=int(year),month=int(month),day=1)
        articles = articles.filter(publish_at__year=year,publish_at__month=month)

    ctx['articles'] = articles.order_by('-publish_at')
    return render(request,template_name,ctx)

def article(request,year,month,article_id,tempalte_name='simpleblog/article.html'):
    article = get_object_or_404(Article,id=article_id,status=1)
    article.num_views += 1
    article.save()
    return render(request,tempalte_name,{'article':article})
