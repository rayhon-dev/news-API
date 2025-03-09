from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'author_email']
    search_fields = ['author_name', 'content']
