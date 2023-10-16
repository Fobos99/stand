from django.contrib import admin
from .models import Director, Filials, First_Zam, Zam

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job')
    list_display_links = ('id', 'title_name')
    

class First_ZamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job')
    list_display_links = ('id', 'title_name')
    

class ZamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job')
    list_display_links = ('id', 'title_name')
    
    
class FilialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job')
    list_display_links = ('id', 'title_name')
    
   
    
# Register your models here.
admin.site.register(Director,DirectorAdmin )
admin.site.register(First_Zam,First_ZamAdmin )
admin.site.register(Zam , ZamAdmin )
admin.site.register(Filials,FilialsAdmin )