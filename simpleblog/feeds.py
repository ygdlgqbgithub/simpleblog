from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from simpleblog.models import Article

class LatestFeed(Feed):
    title = 'simpleblog'
    description = 'mysimpleblog,just for doem'
    link = 'http://mysimpleblog.sinaapp.com'


    def items(self):
        return Article.objects.filter(status=1).order_by("-publish_at")[:10]

    def item_pubdate(self, item):
        return item.publish_at

    def item_description(self,item):
        return item.content



