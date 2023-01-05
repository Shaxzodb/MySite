from django.utils.translation import gettext_lazy as _
from pathlib import Path
import socket
import os

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - un suitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',

    'django_db_logger',
    "phonenumber_field",
    # Axes app can be in any position in the INSTALLED_APPS list.
    'axes',
    'hitcount',
    'crispy_forms',
    "crispy_bootstrap5",
    'django_ckeditor_5',
    # My Apps
    'App.apps.AppConfig',
    'APIs.apps.ApisConfig',
    'Users.apps.UsersConfig',
    'Codes.apps.CodesConfig',
    'Channels.apps.ChannelsConfig',
    'Articles.apps.ArticlesConfig',
    'Comments.apps.CommentsConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'middleware.language.LocaleMiddleware',
    
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.email_verify.EmailVerification',

    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    'axes.middleware.AxesMiddleware',

]

ROOT_URLCONF = 'Config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('Templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'Config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'db_pos',
    #     'USER' : 'postgres',
    #     'PASSWORD' : 'ShaxzodMaster200',
    #     'HOST' : 'localhost',
    #     'PORT' : '5432',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Kirishlar Cheklovi AXES Sozlamalari
AXES_ENABLED = os.getenv('AXES_ENABLED',True)
AXES_FAILURE_LIMIT = 10  # Notug'ri Kirishlar soni
AXES_ACCESS_FAILURE_LOG_PER_USER_LIMIT = 100
# True Agar muvaqiyatli kirish avalgi muvaqiyatsiz kirishlarni uchiradi
AXES_RESET_ON_SUCCESS = True
AXES_ONLY_ADMIN_SITE = False  # True bo'lsa faqat Admin panel uchun urinli
AXES_COOLOFF_TIME = 1  # Soat
AXES_LOCKOUT_TEMPLATE = 'accounts/user_block.html'  # Shablon
AXES_HTTP_RESPONSE_CODE = 429  # Status code
# Agar bo'lsa True, Axes hech qachon HTTP GET so'rovlarini bloklamaydi.
AXES_NEVER_LOCKOUT_GET = True

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# So'rovlar Cheklovi RATELIMIT Sozlamalari
RATELIMIT_VIEW = 'App.views.rate_limited'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': [
            str(os.getenv('REDIS', 'redis://127.0.0.1:6379'))
        ],
        # 'TIMEOUT': 300 ,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# Til Sozlamalari

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
)
LANGUAGE_COOKIE_NAME = '_language'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Xatolar Ustida ishlash
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {

        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 27,
            'backupCount': 3,
            'encoding': 'utf8',
            'filename': BASE_DIR.joinpath('logs/error.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        },
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request': {
            # logging 500 errors to database
            'handlers': ['db_log', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    },
}

# Email Sozlamalari
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST = socket.gethostbyname('smtp.gmail.com')
EMAIL_POST = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Boshqaruvshilar Ruyxati
ADMINS = [('Shaxzod', EMAIL_HOST_USER)]
MANAGERS = [('Shaxzod', EMAIL_HOST_USER)]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfile'))
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
CKEDITOR_5_CONFIGS = {
    'extends_article': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': [
            'heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
            'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
            'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
            'insertTable',
        ],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'mediaEmbed': {'previewsInData': True},
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph',
                    'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1',
                    'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2',
                    'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3',
                    'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    
    'extends_profile':{
        'blockToolbar': [],
        'toolbar': [ 
            'bold', 'italic', 'link','|','fontFamily'
        ],
        
    },
    'list': {   
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'Users.CustomUserModel'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'login'

# Xafsizlik HTTP -> HTTPS
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# CRISPY FORMS FONTS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# default value 7
HITCOUNT_KEEP_HIT_ACTIVE = { 'days': 7 }
# default value
HITCOUNT_KEEP_HIT_IN_DATABASE = { 'days': 30 }