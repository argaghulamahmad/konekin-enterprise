"""konekin_enterprise URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
import company_profile.urls as company_profile
import company_login.urls as company_login
import company_jobs.urls as company_jobs
import company_forum.urls as company_forum
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^company/login/', include(company_login, namespace='company_login')),
    url(r'^company/profile/', include(company_profile, namespace='company-profile')),
    url(r'^company/jobs/', include(company_jobs, namespace='company-jobs')),
    url(r'^company/forum/', include(company_forum, namespace='company-forum')),
    url(r'^$', RedirectView.as_view(url = '/company/login/', permanent = 'true'), name = 'company_login'),
]