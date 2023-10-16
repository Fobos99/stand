from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название услуги ') 
    prewiev = RichTextField(verbose_name='Анонс услуги') 
    detail = RichTextField(verbose_name='Подробнее о услуге услуги') 
    key = models.CharField(max_length=200, verbose_name='Ключ услуги ') 
    image = models.ImageField(upload_to='images/service/' , blank=True , null=True, verbose_name='Иконка услуги')
            
    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
        