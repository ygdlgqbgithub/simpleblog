from django.contrib import  admin

from simpleblog.models import Category,Article

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title','author','category','status','publish_at','created_at')
    search_fields = ('title','category')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce_src.js','/static/js/textareas.js')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)