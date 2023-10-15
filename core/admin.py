from django.contrib import admin
from .models import MenuModel


class ModelInline(admin.TabularInline):
    model = MenuModel


@admin.register(MenuModel)
class ModelAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'parent')
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

    inlines = [
        ModelInline
    ]


