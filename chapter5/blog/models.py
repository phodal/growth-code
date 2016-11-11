from django.db import models
from django.db.models import permalink


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.posted, self.title)

    @permalink
    def get_absolute_url(self):
        return 'blog_view', None, {'slug': self.slug}
