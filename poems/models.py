from django.db import models
from libs.slughifi import slughifi
from django.contrib.auth.models import User
# from easy_thumbnails.fields import ThumbnailerImageField


class Poem(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, blank=True)
    has_title = models.BooleanField(default=False)
    # Num of letters by line, num of lines by strophe, num of strophes
    params = models.CommaSeparatedIntegerField(max_length=5, default='42,6,1')
    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey('userprofile.User', blank=True, \
    # null=True, on_delete=models.SET_NULL)
    # users = models.ManyToManyField('userprofile.User', blank=True, null=True)
    # tags = models.ManyToManyField('tags.Tag', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.has_title is False:
            self.title = self.body[:60]

        self.slug = slughifi(self.title)
        super(Poem, self).save(*args, **kwargs)


class Line(models.Model):
    body = models.CharField(max_length=79)
    poem = models.ForeignKey('Poem')
