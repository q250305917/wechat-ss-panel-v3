"""panelWechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from wechat.views import home, checkToken, createTable, subscribe, getUserInfo, setTemplate, deleteTable, getIndustry

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^checkToken/$', checkToken),
    url(r'^subscribe/$', subscribe),
    url(r'^createTable/$', createTable),
    url(r'^deleteTable/$', deleteTable),
    url(r'^getUserInfo/$', getUserInfo),
    url(r'^setTemplate/$', setTemplate),
    url(r'^getIndustry/$', getIndustry),
    url(r'^admin/', admin.site.urls),

]
