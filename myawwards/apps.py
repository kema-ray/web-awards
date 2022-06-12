from django.apps import AppConfig


class MyawwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myawwards'

from django.apps import AppConfig
 
class UsersConfig(AppConfig):
    name = 'users'
 
    # def ready(self):
    #     import users.signals
