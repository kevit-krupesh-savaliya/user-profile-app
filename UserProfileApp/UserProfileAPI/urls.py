from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/user$', user_create_api),
    url(r'^api/user/(?P<pk>[0-9]+)$', user_details_api),
    url(r'^api/login$', user_login_api),
]
