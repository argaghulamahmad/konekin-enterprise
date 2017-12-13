from django.conf.urls import url
from .views import company_forum,add_forum

urlpatterns = [
    url(r'^add-forum/(?P<id>.*)/$', add_forum, name='add-forum'),
    url(r'^(?P<id>.*)/$', company_forum, name='company-forum'),

]
