"""mehrgan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from blog.urls import urlpatterns as blog_urls
from core.urls import urlpatterns as core_urls
from consultant.urls import urlpatterns as consultant_urls
from mehrgan import settings

admin.site.site_header = "پنل مدیریت مهرگان"
admin.site.site_title = "پنل مدیریت مهرگان"
admin.site.index_title = "پنل مدیریت مهرگان"

default_urls = [path('api/browse/', include('rest_framework.urls')), path('u39723KuSDwdi723dSgoJIuSD3245R7P987AS2n/admin/', admin.site.urls)]
imported_urls = [*blog_urls, *core_urls, *consultant_urls, ]
urlpatterns = [*default_urls] + imported_urls + static(settings.STATIC_URL,
                                                       document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                                    document_root=settings.MEDIA_ROOT)
