from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}