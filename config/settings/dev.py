from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")

SECRET_KEY = config("SECRET_KEY", default="dev-secret-key")