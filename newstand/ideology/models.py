from django.db import models
from distutils.command.upload import upload
from ckeditor.fields import RichTextField
# Create your models here.

class Deskbest(models.Model):
    photo = models.ImageField(upload_to='images/photo/deskbest', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    title_place =  models.CharField(max_length=200 , verbose_name='Агенство/Филиал') 
    is_published = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = 'Доска почёта'
        verbose_name_plural = 'Доска почёта'
        
        
class Bestworker(models.Model):
    photo = models.ImageField(upload_to='images/photo/bestworker', verbose_name='Фото')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО') 
    title_job = models.CharField(max_length=200 , verbose_name='Должность') 
    title_place =  models.CharField(max_length=200 , verbose_name='Агенство/Филиал') 
    is_published = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = 'Лучший по профессии'
        verbose_name_plural = 'Лучший по профессии'
        
        
class Grafik(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название графика')
    post = RichTextField(verbose_name='Описание графика')
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Графики'
        verbose_name_plural = 'График'
        

     
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название новости')
    preview_news = RichTextField(verbose_name='Анонс новости')
    detail_news = RichTextField(verbose_name='Детальная новость')
    date = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(upload_to='images/news/%Y/%m/%d/' , blank=True , null=True, verbose_name='Фото главное' )
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date' , 'title']  
        

class Edi(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название статьи/матерьяла')
    post = RichTextField(verbose_name='Описание статьи/матерьяла')
    date = models.DateTimeField(verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'статья/матерьял'
        verbose_name_plural = 'Статья/Матерьял'
        ordering = ['-date', 'title'] 
        
class Govment(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название символики')
    image = models.ImageField(upload_to='images/govment/%Y/%m/%d/' , blank=True , null=True, verbose_name='Символика')
    description = RichTextField(verbose_name='Описание символики')
    
    class Meta:
        verbose_name = 'Сиволика РБ'
        verbose_name_plural = 'Символика РБ'
        
        
        
class Organizations(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название организации')
    image = models.ImageField(upload_to='images/organizations/%Y/%m/%d/' , blank=True , null=True, verbose_name='Фото для организации')
    description = RichTextField(verbose_name='Описание организации')
    
    class Meta:
        verbose_name = 'Общественные организации'
        verbose_name_plural = 'Общественные организации'
        
class BRSM(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название первичной организации')
    image_brsm = models.ImageField(upload_to='images/organizations/%Y/%m/%d/' , blank=True , null=True, verbose_name='Символика БРСМ №1')
    image_brsm2 = models.ImageField(upload_to='images/organizations/%Y/%m/%d/' , blank=True , null=True, verbose_name='Символика БРСМ №2')
    descr_info = RichTextField(verbose_name='Документация/устав')
    descr_about = RichTextField(verbose_name='Структура БРСМ')
    brsm_symbol = models.ImageField(upload_to='images/brsm/%Y/%m/%d/' , blank=True , null=True, verbose_name='Фото описание символики')
    brsm_bilet = models.ImageField(upload_to='images/brsm/%Y/%m/%d/' , blank=True , null=True, verbose_name='Фото описание билета')
    
    class Meta:
        verbose_name = 'БРСМ инфо'
        verbose_name_plural = 'БРСМ инфо'
        
class BRSM_contacts(models.Model):
    title_org = models.CharField(max_length=200 , verbose_name='Организация')
    title_adress = models.CharField(max_length=200 , verbose_name='Адресс')
    title_email = models.CharField(max_length=200 , verbose_name='почта')
    title_job = models.CharField(max_length=200 , verbose_name='Должность')
    title_name = models.CharField(max_length=200 , verbose_name='ФИО')
    photo = models.ImageField(upload_to='images/photo/brsm-contacts', verbose_name='Фото')
    
    class Meta:
        verbose_name = 'Контакты БРСМ'
        verbose_name_plural = 'Контакты БРСМ'