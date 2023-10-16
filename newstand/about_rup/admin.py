from django.contrib import admin
from .models import Functions, About_rup, Map, Terretory
# Register your models here.


class FunctionsAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    
class About_rupAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
  
  
class MapAdmin(admin.ModelAdmin):
    list_display = ('id' ,'image_map' )
    list_display_links = ('id' ,'image_map')  
    
class TerretoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' )
    list_display_links = ('id' ,'title')  
    



admin.site.register(Functions, FunctionsAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(About_rup, About_rupAdmin)
admin.site.register(Terretory, TerretoryAdmin)