from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserprofileapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserProfileAPI'
    verbose_name = _('UserProfileAPI')
