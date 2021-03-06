# Django settings for djangoapp project.
import socket
import os

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Eduardo Gonzalo Espinoza Carreon', 'edubecks007@gmail.com'),
)

MANAGERS = ADMINS

DATABASES  = {}

## local dev
if (
    socket.gethostname() == 'SpiderMac.local'
    ):
    DEBUG =  True

    ## database
    DB_NAME =       os.getenv('CARONAS_BRASIL_DB_NAME')
    DB_USER =       os.getenv('CARONAS_BRASIL_DB_USER')
    DB_PASSWORD =   os.getenv('CARONAS_BRASIL_DB_PASSWORD')
    DB_HOST =       os.getenv('CARONAS_BRASIL_DB_HOST')
    DB_PORT =       os.getenv('CARONAS_BRASIL_DB_PORT')
    DB_ENGINE =     os.getenv('CARONAS_BRASIL_DB_ENGINE')

    DATABASES['default'] =  {
            'ENGINE': DB_ENGINE, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': DB_PORT,                      # Set to empty string for default.
        }

else:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.vaidecarona.org', 'caronasbrasil.herokuapp.com', 'localhost', 'loc-caronasbrasil.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'https://s3.amazonaws.com/caronas-brasil/staticfiles/'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.path.pardir))
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, 'staticfiles/'))

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(PROJECT_DIR, 'static/')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('CARONAS_BRASIL_DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangoapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'djangoapp.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '..//', 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'djangoapp.apps.caronasbrasil',
    'south',
    # 'social.apps.django_app.default',
    ## production
    'gunicorn',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#
# ## facebook login
# ## social auth
# ## http://psa.matiasaguirre.net/docs/backends/facebook.html#oauth2
# SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('CARONAS_BRASIL_FB_APP_ID')
# SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('CARONAS_BRASIL_FB_APP_SECRET')
#
#
# AUTHENTICATION_BACKENDS = (
#     'social.backends.facebook.FacebookOAuth2',
#     # 'social.apps.django_app.utils.BackendWrapper',
# )
#
#
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.contrib.messages.context_processors.messages',
#     'social.apps.django_app.context_processors.backends',
# )
#
#
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/done/'
# URL_PATH = ''
# SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
# SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
# SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
#     'https://www.googleapis.com/auth/drive',
#     'https://www.googleapis.com/auth/userinfo.profile'
# ]
# # SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
# SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
# SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
# SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# # SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
# SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'
#
# SOCIAL_AUTH_PIPELINE = (
#     # 'social.pipeline.social_auth.social_details',
#     # 'social.pipeline.social_auth.social_uid',
#     # 'social.pipeline.social_auth.auth_allowed',
#     # 'social.pipeline.social_auth.social_user',
#     # 'social.pipeline.user.get_username',
#     # 'example.app.pipeline.require_email',
#     # 'social.pipeline.mail.mail_validation',
#     # 'social.pipeline.user.create_user',
#     # 'social.pipeline.social_auth.associate_user',
#     # 'social.pipeline.social_auth.load_extra_data',
#     # 'social.pipeline.user.user_details'
# )
