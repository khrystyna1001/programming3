import environ
import os

from django.db.models import TextChoices

class EnvironmentType(TextChoices):
    SETTINGS = "settings"

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True),
    ENVIRONMENT=(EnvironmentType, EnvironmentType.SETTINGS),
    WORKING_INSIDE_CONTAINER = [bool, False]
)

__all__ = ["env"]