from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/user$', user_details_api, name="user-details"),
    url(r'^api/user/create$', user_create_api, name="user-create"),
    url(r'^api/user/login$', user_login_api, name="user-login"),
]
