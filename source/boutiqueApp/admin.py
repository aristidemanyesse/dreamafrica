from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['__str__', "deleted", "created_at"]


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "price", "description", "categorie", "deleted",  "created_at"]