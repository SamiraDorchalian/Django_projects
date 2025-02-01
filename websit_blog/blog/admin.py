from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_created', 'datetime_modified', 'author', )
    ordering = ('status', )

# Register your models here.
# admin.site.register(Post, PostAdmin)

