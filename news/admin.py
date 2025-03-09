from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'views_count', 'category']
    search_fields = ['title', 'content', 'tags']
    prepopulated_fields = {"slug": ("title",)}


