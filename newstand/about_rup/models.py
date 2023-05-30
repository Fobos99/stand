from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Terretory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Агентство\филиал\бюро ') 
    terretory = RichTextField(verbose_name='Территория обслуживания ') 
    adress= models.CharField(max_length=200, verbose_name='Адресс ') 
    tel= models.CharField(max_length=200, verbose_name='Телефон ') 
    mail= models.CharField(max_length=200, verbose_name='Эл.почта ') 
    rs_bank= RichTextField(verbose_name='Расчётный счёт банка ' ,  blank=True , null=True) 
            
    class Meta:
        verbose_name = 'ТОРы'
        verbose_name_plural = 'ТОРы'
        
        
        
        
class Functions(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название функций') 
    description = RichTextField(verbose_name='Функции предприятия')    
            
    class Meta:
        verbose_name = 'Функции предприятия'
        verbose_name_plural = 'Функции предприятия'
        
        
        
        
class About_rup(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название о нас') 
    description = RichTextField(verbose_name='Описание')    
            
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        
        
        
        
class Map(models.Model):
    image_map = models.ImageField(upload_to='images/about/' , blank=True , null=True, verbose_name='Карта области')
    
    class Meta:
        verbose_name = 'Карта области'
        verbose_name_plural = 'Карта области'