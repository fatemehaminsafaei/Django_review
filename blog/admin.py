from django.contrib import admin
from blog.models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['auther', 'title', 'text', 'created_date', 'published_date', 'status', 'thumbnail']
