"""Index_9071 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import responses as rps
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls import handler404 as h404
from django.conf.urls import handler500 as h500

h404 = rps.page404
h500 = rps.page404

urlpatterns = [
    url(r'^/whoisadmin/', admin.site.urls),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'src/favicon.ico')),
    url(r'^aboutus$',rps.aboutus),
    url(r'^intro$',rps.aboutfrc),
    url(r'^404$',rps.page404),
    url(r'^$', rps.index, name='home'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
