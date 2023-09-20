from django.contrib import admin
from core.models.card import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
