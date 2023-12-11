from django.contrib import admin

from coreApp.models import Etat

# Register your models here.


@admin.register(Etat)
class EtatAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_display = ["name", "etiquette",]
    