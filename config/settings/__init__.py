from decouple import config

ENVIRONMENT = config("ENVIRONMENT", default="development")

if ENVIRONMENT == "production":
    from .prod import *
else:
    from .dev import *