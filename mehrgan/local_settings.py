# SECURITY WARNING: keep the secret key used in production secret!
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'zv2^004ts_4i_!ocbwfh50@j5)8^pafkc#j(0@35ckdjem&rg&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mehrgan',
        'USER': 'root',
        'PASSWORD': '15015',
        'HOST': 'localhost'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets")


MEDIA_URL = '/medias/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')


UPLOAD_DIRECTORIES = {
    'blog_thumbnail': 'blog_thumbnail',
    'category_thumbnail': 'category_thumbnail',
}
