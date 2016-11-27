# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    class Meta:
        verbose_name = _('博客')
        verbose_name_plural = _('博客')

    title = models.CharField(max_length=30, unique=True, verbose_name=_('标题'), help_text='博客的标题')
    author = models.ForeignKey(User, verbose_name=_('作者'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('URL'))
    body = models.TextField(verbose_name=_('正文'))
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return 'blog_view', None, {'slug': self.slug}
