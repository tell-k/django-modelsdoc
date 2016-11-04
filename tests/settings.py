from django import VERSION

DEBUG = False

if VERSION < (1, 10):
    TEMPLATE_DEBUG = False
else:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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


# for django 1.5
ROOT_URLCONF = 'urls'
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    'modelsdoc',
    'tests',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

if VERSION >= (1, 6):
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
else:
    TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

SECRET_KEY = 'secret_key_for_testing'
MIDDLEWARE_CLASSES = []

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
