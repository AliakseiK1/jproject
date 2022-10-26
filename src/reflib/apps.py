from django.apps import AppConfig

from proj.settings import DEFAULT_AUTO_FIELD


class ReflibConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reflib'
class MainpageConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    name = 'mainpage'