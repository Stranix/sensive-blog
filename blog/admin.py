from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']
    list_display = ['title', 'published_at']
    raw_id_fields = ['tags', 'author', 'likes']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'published_at']
    raw_id_fields = ['post', 'author']


admin.site.register(Tag)
