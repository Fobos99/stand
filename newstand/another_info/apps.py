from django.apps import AppConfig


class AnotherInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'another_info'
    verbose_name = 'Доп информация'
