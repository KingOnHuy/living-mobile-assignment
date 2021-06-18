from django.contrib import admin
from .models import *

admin.site.site_header = "Living Mobile administration"
admin.site.site_title = "Living Mobile"


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.fields]
    search_fields = [
        'name',
        'description',
    ]
    list_filter = [
        'rating'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    search_fields = [
        'name',
    ]
    list_filter = [
        'storeId'
    ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Menu._meta.fields]
    search_fields = [
        'name',
    ]
    list_filter = [
        'categoryId'
    ]
