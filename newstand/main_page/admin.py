from django.contrib import admin
from .models import Services
# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'key' )
    list_display_links = ('id' ,'title' , 'key')  
   
   
   
   
admin.site.register(Services, ServicesAdmin)