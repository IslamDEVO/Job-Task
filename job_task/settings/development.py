from .base import *

DEBUG = True

# Add New Apps To INSTALLED_APPS
INSTALLED_APPS.append('accounts.apps.AccountsConfig')
INSTALLED_APPS.append('pages.apps.PagesConfig')

# Add Third-party
INSTALLED_APPS.append('crispy_forms')
# Django Crispy-Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Add Third-party django-allauth That Contain social authentication --------------
INSTALLED_APPS.append('django.contrib.sites')
INSTALLED_APPS.append('allauth')
INSTALLED_APPS.append('allauth.account')
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
TEMPLATES[0]["OPTIONS"]['context_processors'].append('django.template.context_processors.request')
SITE_ID = 1
ACCOUNT_LOGOUT_REDIRECT = 'home' #
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new
ACCOUNT_SESSION_REMEMBER = True # new
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # new
ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email' # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new

# Add Templates Directory Settings -------------------------------
TEMPLATES[0]["DIRS"] = [BASE_DIR.joinpath('../templates')]

# Tell Django to user CustomUser instead of the default User model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Tell Django to redirct logged in user to the homepage
LOGIN_REDIRECT_URL = 'home'
# Tell Django to redirct logged out in user to the homepage
LOGOUT_REDIRECT_URL = 'home'

# Tell Django Where Static Directory ------------------------------
STATIC_URL = '/static/'
# Location of static files in local development
STATICFILES_DIRS = (str(BASE_DIR.joinpath('../static')),)
# Location of static files for production, when ues collectstatic command
STATIC_ROOT = str(BASE_DIR.joinpath('../staticfiles'))
# which tells django how to look for static file directories
STATICFILES_FINDERS = [ 
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Setting Mail For EmailBackend
DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'