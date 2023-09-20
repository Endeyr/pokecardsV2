from django.contrib import admin
from core.models.collection import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
    )
