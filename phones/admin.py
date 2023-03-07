from django.contrib import admin
from .models import Phone
# Register your models here.

@admin.register(Phone)
class Phone(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists']
    list_filter = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}