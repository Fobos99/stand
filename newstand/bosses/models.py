from django.db import models
from distutils.command.upload import upload



# Create your models here.
class Director(models.Model):
    photo = models.ImageField(upload_to='images/photo/bosses', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО директора') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    is_published = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = 'Руководство, директор'
        verbose_name_plural = 'Руководство, директор'
        

class First_Zam(models.Model):
    photo = models.ImageField(upload_to='images/photo/bosses', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО 1-го зама') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    is_published = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = 'Руководство, 1-й заместитель'
        verbose_name_plural = 'Руководство, 1-й заместитель'
     
        
class Zam(models.Model):
    photo = models.ImageField(upload_to='images/photo/bosses', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО заместителя') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    is_published = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = 'Руководство,  заместитель'
        verbose_name_plural = 'Руководство, заместитель'
        
        
class Filials(models.Model):
    photo = models.ImageField(upload_to='images/photo/bosses', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО начальника филиала') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    title_place =  models.CharField(max_length=200 , verbose_name='Агенство/Филиал') 
    is_published = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = 'Руководство, начальник филиала'
        verbose_name_plural = 'Руководство, начальник филиала'
       