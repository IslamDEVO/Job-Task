from .base import *

DEBUG = True

INSTALLED_APPS.append(
    # Local
    'accounts.apps.AccountsConfig'
)

# Tell Django to user CustomUser instead of the default User model
AUTH_USER_MODEL = 'accounts.CustomUser'     # New