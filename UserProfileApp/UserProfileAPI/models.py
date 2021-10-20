import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("user ID"))
    name = models.CharField(max_length=60, blank=False, verbose_name=_("name"))
    email = models.CharField(max_length=60, blank=False, unique=True, verbose_name=_("Email"))
    phone_no = models.FloatField(max_length=10, blank=False, unique=True, verbose_name=_("phone Number"))
    password = models.CharField(max_length=100, blank=False, verbose_name=_("Password"))
    gender = models.CharField(max_length=6, default='Male', verbose_name=_("gender"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
