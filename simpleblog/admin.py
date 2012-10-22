from django.contrib import  admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

from simpleblog.models import Category,Article



class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title','author','category','status','publish_at','created_at')
    search_fields = ('title','category')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce_src.js',
              '/static/js/textareas.js')
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class FlatPageTinymceAdmin(FlatPageAdmin):
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce_src.js',
              '/static/js/textareas.js')
              
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage,FlatPageTinymceAdmin)

