from django.contrib import admin

from .models import Book, Comment

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publisher','translator','price','pages_book', 'year_of_publication', 'cover', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', )

admin.site.register(Book, BookAdmin)
# admin.site.register(Comment, CommentAdmin)



