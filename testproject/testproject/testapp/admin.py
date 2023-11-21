from django.contrib import admin
from .models import place, person


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')  # Customize the fields displayed in the list view


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')  # Customize the fields displayed in the list view


admin.site.register(place, PlaceAdmin)
admin.site.register(person, PersonAdmin)
