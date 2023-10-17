from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter



@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "price", "description",  "deleted",  "created_at"]

@admin.register(FaqProduit)
class ProduitAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["produit", "question", "reponse",  "created_at"]