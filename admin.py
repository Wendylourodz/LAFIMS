from django.contrib import admin
from .models import LostItem, FoundItem, ClaimedItem
from .models import Item

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'email', 'date_lost', 'location']

@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'email', 'date_found', 'location']

@admin.register(ClaimedItem)
class ClaimedItemAdmin(admin.ModelAdmin):
    list_display = ['image', 'name']

