from .base import *

import os

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("POSTGRES_ENGINE"),
#         "NAME": os.getenv("POSTGRES_DB"),
#         "USER": os.getenv("POSTGRES_USER"),
#         "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
#         "HOST": os.getenv("PG_HOST"),
#         "PORT": os.getenv("PG_PORT"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
