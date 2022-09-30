import sys
import os
sys.path.append(os.getcwd())
from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals
