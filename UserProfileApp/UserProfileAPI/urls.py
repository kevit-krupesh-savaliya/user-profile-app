from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', user_create_api),
    url(r'^(?P<pk>[0-9]+)$', user_details_api),
    url(r'^login$', user_login_api),
]
