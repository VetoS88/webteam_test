from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Categories, Articles


@admin.register(Categories)
class CategoriesAdmin(ModelAdmin):
    list_display = ['id', 'name', 'h1', 'slug']
    fieldsets = (
        (None,
         {'fields': ('name', 'h1',)}
         ),
    )
    add_fieldsets = (
        (None, {'fields': ('name', 'h1',)}),
    )
    list_display_links = ['id', ]


@admin.register(Articles)
class ArticlesAdmin(ModelAdmin):
    list_display = ['id', 'name', 'h1', 'slug']
    fieldsets = (
        (None,
         {'fields': ('name', 'category', 'h1', 'text', 'slug', 'img')}
         ),
    )
    add_fieldsets = (
        (None, {'fields': ('category', 'name', 'h1',)}),
    )
    list_display_links = ['id', ]
