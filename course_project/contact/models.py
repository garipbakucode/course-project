from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    full_name = models.CharField(
        _('ad soyad'),
        max_length=50,
    )
    email = models.EmailField(
        _('email'),
        max_length=100,
    )
    message = models.TextField(
        _('mətn')
    )
    phone_number = models.CharField(
        _('telefon'),
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        _('created date'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Müraciət')
        verbose_name_plural = _('Müraciətlər')
