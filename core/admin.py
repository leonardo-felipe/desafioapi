from django.contrib import admin

from core.models import Item

class Items(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_quantity')
    search_fields = ('item_name',)
    
admin.site.register(Item, Items)

