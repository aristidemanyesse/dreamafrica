from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import DateFieldListFilter

@admin.register(Participation)
class ParticipantAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["fullname", "email", "contact", "evenement", "deleted",  "created_at"]


@admin.register(ReservationStand)
class ReservationStandAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["fullname", "email", "contact", "evenement", "deleted",  "created_at"]
    
    

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["name", "price", "description",  "deleted",  "created_at"]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["id", "question", "created_at"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["title", "subtitle", "created_at"]

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ["fullname", "email", "contact", "objet", "created_at"]