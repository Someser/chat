import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '4+5ntpkz@8+$h*^&n29klvurp6wajz+)7hrfksb628v)*^f=!b'
DEBUG = True

ALLOWED_HOSTS = []


NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS = getattr(settings, 'NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS', True)

MSG_TYPE_MESSAGE = 0  # For standard messages
MSG_TYPE_WARNING = 1  # For yellow messages
MSG_TYPE_ALERT = 2  # For red & dangerous alerts
MSG_TYPE_MUTED = 3  # For just OK information that doesn't bother users
MSG_TYPE_ENTER = 4  # For just OK information that doesn't bother users
MSG_TYPE_LEAVE = 5  # For just OK information that doesn't bother users

MESSAGE_TYPES_CHOICES = getattr(settings, 'MESSAGE_TYPES_CHOICES', (
    (MSG_TYPE_MESSAGE, 'MESSAGE'),
    (MSG_TYPE_WARNING, 'WARNING'),
    (MSG_TYPE_ALERT, 'ALERT'),
    (MSG_TYPE_MUTED, 'MUTED'),
    (MSG_TYPE_ENTER, 'ENTER'),
    (MSG_TYPE_LEAVE, 'LEAVE')))

MESSAGE_TYPES_LIST = getattr(settings, 'MESSAGE_TYPES_LIST',
                             [MSG_TYPE_MESSAGE,
                              MSG_TYPE_WARNING,
                              MSG_TYPE_ALERT,
                              MSG_TYPE_MUTED,
                              MSG_TYPE_ENTER,
                              MSG_TYPE_LEAVE])
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'messanger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
redis_host = os.environ.get('REDIS_HOST', 'localhost')

CHANNEL_LAYERS = {
    "default": {

        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(redis_host, 6379)],
        },
       "ROUTING": "chat.routing.channel_routing", 
    },
}
