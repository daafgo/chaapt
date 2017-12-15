#!/usr/bin/python
# -*- coding: latin-1 -*-
"""chaapt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
import chat.views
import usuarios.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^$', chat.views.home, name='Home'),
url(r'^(?P<user_id>\d+)/$',chat.views.userchats),
url(r'^(?P<user_id>\d+)/(?P<chat_id>\d+)/$',chat.views.chatv),
url(r'^new/(?P<user_id>\d+)/(?P<rec_id>\d+)/$',chat.views.newchat),

#urls modulo usuarios
url(r'^profile/(?P<user_id>\d+)/$',usuarios.views.profile),
#añadimos la url para servir las imagenes
url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
#emoji urls
url(r'^emoji/', include('emoji.urls')),
]