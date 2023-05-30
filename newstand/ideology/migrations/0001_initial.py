# Generated by Django 4.2 on 2023-04-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bestworker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/photo/bestworker', verbose_name='Фото')),
                ('title_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('title_job', models.CharField(max_length=200, verbose_name='Должность')),
                ('title_place', models.CharField(max_length=200, verbose_name='Агенство/Филиал')),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Лучший по профессии',
                'verbose_name_plural': 'Лучший по профессии',
            },
        ),
        migrations.CreateModel(
            name='Deskbest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/photo/deskbest', verbose_name='Фото')),
                ('title_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('title_job', models.CharField(max_length=200, verbose_name='Должность')),
                ('title_place', models.CharField(max_length=200, verbose_name='Агенство/Филиал')),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Доска почёта',
                'verbose_name_plural': 'Доска почёта',
            },
        ),
    ]