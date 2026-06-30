from .base import *
import os
from decouple import config

DEBUG = False

SECRET_KEY = config("SECRET_KEY", default="dev-secret-key")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: v.split(","))

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
