from django.contrib import admin
from .models import Post


class BlogAdmin (admin.ModelAdmin):
    fields = ['author' , 'title' , 'text' , 'published_date']
    list_filter = ['published_date']

admin.site.register(Post, BlogAdmin)
