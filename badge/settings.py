"""
Django settings for badge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.urlresolvers import reverse_lazy
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.conf import global_settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vm_q$eg7l9$*(#%si5ecp)(v!#q=t0(a=q3b5mpf0t-7)!mqay'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djangobower',
    'rest_framework',
    'crispy_forms',
    'django_gravatar',

    'badges',
    'users',
)



STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + ('djangobower.finders.BowerFinder', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'badge.urls'

WSGI_APPLICATION = 'badge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'badges',
        'USER': 'root',
        'PASSWORD': 'sql123.',
        'CHARSET': 'utf8',
        'OPTIONS': {

        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ro-ro'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, "css")),
    ("js", os.path.join(STATIC_ROOT, "js")),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

BOWER_PATH = '/usr/local/bin/bower'
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'masonry',
    'angularjs',
    'fontawesome',
    'moment',
    'angular-ui',
    'angular-ui-bootstrap',
    'lodash',
    'angular-resource',
    'angular-masonry',
    'angular-moment',
    'ngInfiniteScroll'
)

TEMPLATE_DIRS = global_settings.TEMPLATE_DIRS + (os.path.join(BASE_DIR, "templates"), )


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGINATE_BY': 10,                 # Default to 10
#    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
#    'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
}

CRISPY_TEMPLATE_PACK = "bootstrap3"
SITE_ID = 1
LOGIN_REDIRECT_URL = reverse_lazy("badges:index")
LOGIN_URL = reverse_lazy("users:login")

TEMPLATE_CONTEXT_PROCESSOR = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request", "users.context_processors.url_root")