# admin.py
from django.contrib import admin
from .models import InventoryItem, Category
from .forms import InventoryItemForm

class InventoryItemAdmin(admin.ModelAdmin):
    form = InventoryItemForm

admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(Category)
