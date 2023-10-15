from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter


@admin.register(CategorieItem)
class CategorieItemAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__', "deleted", "created_at"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "lieu", "description", "categorie", "deleted",  "created_at"]