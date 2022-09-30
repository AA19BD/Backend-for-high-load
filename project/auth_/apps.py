import sys
import os
sys.path.append(os.getcwd())
from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth_'

    def ready(self):
        import auth_.signals
        # from . import signals