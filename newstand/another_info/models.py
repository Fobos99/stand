from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Bank(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название ') 
    description = RichTextField(verbose_name='Описание реквизитов')
    
    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'
        
        
        
class About_message(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название ') 
    description = RichTextField(verbose_name='О работе с обращениями')
    
    class Meta:
        verbose_name = 'О работе с обращениями'
        verbose_name_plural = 'О работе с обращениями'



class Dop_info(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название ') 
    description = RichTextField(verbose_name='Дополнительная инфрмация')
    
    class Meta:
        verbose_name = 'Дополнительная инфрмация'
        verbose_name_plural = 'Дополнительная инфрмация'
        
        
        
class El_message(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название ') 
    description = RichTextField(verbose_name='Электронные обращения')
    
    class Meta:
        verbose_name = 'Электронные обращения'
        verbose_name_plural = 'Электронные обращения'