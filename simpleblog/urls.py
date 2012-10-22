from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

from simpleblog.feeds import LatestFeed
from simpleblog import settings


urlpatterns = patterns('simpleblog.views',
     url(r'^$','index',name='simpleblog_index'),
     url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<article_id>\d+)/$',
         'article',name='simpleblog_article' ),

     url(r'^articles/tag/(?P<tag_name>[-\w]+)/$','index',name='simpleblog_tag'),
     url(r'^articles/category/(?P<category_id>\d+)/$','index',
         name='simpleblog_category'),

     url(r'^articles/archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$','index',
         name='simpleblog_archive' ),

     url(r'^latest/feed/$', LatestFeed(), name="simpleblog_feeds"),

     url(r'^admin/', include(admin.site.urls)),
     url(r'^admin/filebrowser/', include(site.urls)),
     url(r'^grappelli/', include('grappelli.urls')),

)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)/$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}))
