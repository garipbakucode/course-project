from typing import Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(
        _('ad'),
        max_length=255,
    )
    last_name = models.CharField(
        _('soyad'),
        max_length=255,
    )
    image = models.ImageField(
        _('şəkil'),       
        upload_to='authors',
    )
    slug = models.SlugField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = _('Yazar')
        verbose_name_plural = _('Yazarlar')


class Blog(models.Model):
    author = models.ForeignKey(
        'account.Account',
        related_name='blogs',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        _('başlıq'),
        max_length=255,
    )
    description = models.TextField(
        _('mətn'),
    )
    image = models.ImageField(
        _('şəkil'),       
        upload_to='blogs',
    )
    slug = models.SlugField()
    published_at = models.DateField(null=True, blank=True)
    category = models.ManyToManyField(
        'blog.Category',
        related_name='blogs'
    )

    def __str__(self):
        return self.title
    # gözəl günlər => gozel-gunler
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Bloq')
        verbose_name_plural = _('Bloqlar')


class Category(models.Model):
    name = models.CharField(
        _('ad'),
        max_length=255,
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Kateqoriya')
        verbose_name_plural = _('Kateqoriyalar')
