from django.contrib import admin
from models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
  #  fields = ('title', 'desc', 'content',)

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
            )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(comment)
admin.site.register(Link)
admin.site.register(Ad)