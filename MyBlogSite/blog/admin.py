from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "photo")
    list_filter = ("category", "photo")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'rating')
    list_filter = ('post', "rating")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)