from django.contrib import admin
from .models import Bank, About_message, El_message, Dop_info
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    
class About_messageAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    
    
class Dop_infoAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    
    
class El_messageAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    
    

admin.site.register(Bank, BankAdmin)
admin.site.register(About_message, About_messageAdmin)
admin.site.register(Dop_info, Dop_infoAdmin)
admin.site.register(El_message, El_messageAdmin)