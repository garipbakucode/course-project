from django.db import models
from django.utils.translation import gettext_lazy as _


class HomePage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('başlıq'), 
    )
    description = models.TextField(
        _('mətn'),
    )
    image = models.ImageField(
        _('şəkil'),       
        upload_to='homeBanner',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Ana səhifə banner')
        verbose_name_plural = _('Ana səhifə banner')


class BelowBanner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('başlıq'), 
    )
    description = models.TextField(
        _('mətn'),
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Bannerin altındakı 3 yazı')
        verbose_name_plural = _('Bannerin altındakı 3 yazı')


class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('başlıq'), 
    )
    image = models.ImageField(
        _('şəkil'),       
        upload_to='about',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Haqqımızda')
        verbose_name_plural = _('Haqqımızda')


class AboutPoint(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('başlıq'), 
    )
    description = models.TextField(
        _('mətn'),       
    )
    about = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        related_name='points'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Haqqımızda punkt')
        verbose_name_plural = _('Haqqımızda punktlar')


class ClientFeedback(models.Model):
    full_name = models.CharField(
        _('ad soyad'),
        max_length=255,
    )
    feedback = models.TextField(
        _('mətn')
    )
    image = models.ImageField(
        _('şəkil'),
        upload_to='clientFeedback',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Müştəri rəyləri')
        verbose_name_plural = _('Müştəri rəyləri')
