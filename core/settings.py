from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0zb$=#s$@2lfr1yu!6ax8)pgk3sz3r5qbm=yn+k==06+lgg&d@'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---- UNFOLD ADMIN THEME (Казына: emerald + gold) ----
UNFOLD = {
    "SITE_TITLE": "Казына Admin",
    "SITE_HEADER": "КАЗЫНА",
    "SITE_SUBHEADER": "Управление рестораном",
    "SITE_URL": "/",
    "SITE_SYMBOL": "restaurant",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,
    "COLORS": {
        "font": {
            "subtle-light":    "120 113 92",
            "subtle-dark":     "168 162 142",
            "default-light":   "75 69 50",
            "default-dark":    "220 210 180",
            "important-light": "17 24 12",
            "important-dark":  "245 240 220",
        },
        "primary": {
            "50":  "240 250 244",
            "100": "209 240 222",
            "200": "166 222 191",
            "300": "110 196 152",
            "400": "55 163 110",
            "500": "2 62 42",
            "600": "1 50 33",
            "700": "1 40 26",
            "800": "1 30 18",
            "900": "0 20 12",
            "950": "0 12 7",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Контент сайта",
                "separator": True,
                "items": [
                    {"title": "Меню (блюда)",      "icon": "restaurant_menu", "link": "/admin/restaurant/menuitem/"},
                    {"title": "Категории меню",    "icon": "category",        "link": "/admin/restaurant/category/"},
                    {"title": "Залы / Атмосфера",  "icon": "meeting_room",    "link": "/admin/restaurant/hall/"},
                    {"title": "Галерея",            "icon": "photo_library",   "link": "/admin/restaurant/galleryimage/"},
                    {"title": "Слайды баннера",    "icon": "slideshow",       "link": "/admin/restaurant/sliderslide/"},
                    {"title": "Настройки сайта",   "icon": "settings",        "link": "/admin/restaurant/sitesettings/"},
                ],
            },
            {
                "title": "Пользователи",
                "separator": True,
                "items": [
                    {"title": "Пользователи", "icon": "person", "link": "/admin/auth/user/"},
                    {"title": "Группы",       "icon": "group",  "link": "/admin/auth/group/"},
                ],
            },
        ],
    },
}
