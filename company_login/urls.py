from django.conf.urls import url
from .views import index,addCompanyData

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^company/data', addCompanyData, name= 'addCompanyData'),
]