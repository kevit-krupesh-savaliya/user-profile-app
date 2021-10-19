from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'user/', include('UserProfileAPI.urls')),
    path('admin/', admin.site.urls),
]
