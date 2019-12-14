from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
    	# create groups after migration
        from .signals import create_groups
        post_migrate.connect(create_groups, sender=self)
