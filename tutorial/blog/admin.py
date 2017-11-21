from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

# Register your models here.
admin.site.register(Article, ArticleAdmin)
