from django.contrib import admin

from .models import Category, Vehicle


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
