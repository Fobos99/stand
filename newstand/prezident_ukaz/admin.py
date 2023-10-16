from django.contrib import admin
from .models import Prez_ukaz
# Register your models here.


class Prez_ukazAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Prez_ukaz, Prez_ukazAdmin)
