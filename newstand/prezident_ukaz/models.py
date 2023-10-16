from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Prez_ukaz(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название ')
    description = RichTextField(verbose_name='Указ президента')

    class Meta:
        verbose_name = 'Указ президента'
        verbose_name_plural = 'Указ президента'
