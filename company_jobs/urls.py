from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<id>.*)/$', company_jobs, name='company-jobs')
]