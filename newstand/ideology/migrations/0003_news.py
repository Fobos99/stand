# Generated by Django 4.2 on 2023-05-02 05:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideology', '0002_grafik'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название новости')),
                ('post', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/news/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date', 'title'],
            },
        ),
    ]
