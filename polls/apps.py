"""This module is for poll configuration."""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """AppConfig for the 'polls' app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
