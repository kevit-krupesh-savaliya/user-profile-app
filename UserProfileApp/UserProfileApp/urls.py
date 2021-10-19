from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    url(r'^', include('UserProfileAPI.urls')),
    path('admin/', admin.site.urls),

    prefix_default_language=False
)
