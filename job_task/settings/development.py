from .base import *

DEBUG = True

# Add New Apps To INSTALLED_APPS
INSTALLED_APPS.append('accounts.apps.AccountsConfig')
INSTALLED_APPS.append('pages.apps.PagesConfig')

# Add Templates Directory Settings
TEMPLATES[0]["DIRS"] = [BASE_DIR.joinpath('../templates')]

# Tell Django to user CustomUser instead of the default User model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Tell Django to redirct logged in user to the homepage
LOGIN_REDIRECT_URL = 'home'
# Tell Django to redirct logged out in user to the homepage
LOGOUT_REDIRECT_URL = 'home'