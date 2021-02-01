from django.contrib import admin
from .models import Post, Writer

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','writer','status','publish_date']
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title','writer')}

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name','last_name')}
