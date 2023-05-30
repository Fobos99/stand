from django.contrib import admin
from .models import Deskbest, Bestworker, Grafik, News, Edi, Govment, BRSM, BRSM_contacts, Organizations
# Register your models here.
class DeskbestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job', 'title_place')
    list_display_links = ('id', 'title_name')
    search_fields = ('title_name', 'title_job', 'title_place')
    """  list_editable = ('is_published',) """


class BestworkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name' , 'title_job', 'title_place')
    list_display_links = ('id', 'title_name')
    search_fields = ('title_name', 'title_job', 'title_place')
    """  list_editable = ('is_published',) """
    
class GrafikAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' )
    list_display_links = ('id', 'title')    
    """  list_editable = ('is_published',) """
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'post')    
    list_filter = ('date',)
    """ list_editable = ('is_published',) """

class EdiAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'post')    
    list_filter = ('date',)
    """ list_editable = ('is_published',) """   
    
class GovmentAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title')
    list_display_links = ('id', 'title')  

class BRSMAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title')
    list_display_links = ('id', 'title')    
    """ list_editable = ('is_published',) """ 

class BRSM_contactsAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title_org', 'title_name', 'title_job')
    list_display_links = ('id', 'title_org') 
    """ list_editable = ('is_published',) """ 

class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title')
    list_display_links = ('id', 'title')  



admin.site.register(Deskbest, DeskbestAdmin)
admin.site.register(Bestworker,  BestworkerAdmin)
admin.site.register(Grafik, GrafikAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Edi, EdiAdmin)
admin.site.register(Govment, GovmentAdmin)
admin.site.register(BRSM, BRSMAdmin)
admin.site.register(BRSM_contacts, BRSM_contactsAdmin)
admin.site.register(Organizations, OrganizationsAdmin)