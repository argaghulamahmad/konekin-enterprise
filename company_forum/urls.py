from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<id>.*)/$', company_forum, name='company-forum'),
    url(r'^add-forum/(?P<id>.*)/$', add_forum, name='add_forum'),

]
