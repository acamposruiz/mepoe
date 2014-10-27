from django.db import models
from libs.slughifi import slughifi
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from easy_thumbnails.fields import ThumbnailerImageField


class Author(models.Model):
    name = models.CharField(max_length=50)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name


class Poem(models.Model):
    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=60, blank=True)
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)
    body = models.TextField(max_length=10000)
    slug = models.SlugField(max_length=100, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poem_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        if not self.title:
            self.title = self.body[:(self.body.index('/') or 60)].strip(',.:;')

        self.slug = slughifi(self.title)
        super(Poem, self).save(*args, **kwargs)
