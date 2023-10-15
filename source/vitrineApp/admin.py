from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "deleted", "created_at"]

@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name', "edition",  "deleted", "created_at"]

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['titre', "soustitre", "auteur", "deleted", "created_at"]


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["fullname", "fonction", "email", "contact", "type", "deleted",  "created_at"]


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "email", "contact", "categorie", "edition", "deleted",  "created_at"]
    
    
@admin.register(CategorieStand)
class CategorieStandAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "deleted",  "created_at"]


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "jour", "description",  "deleted",  "created_at"]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["id", "question", "created_at"]