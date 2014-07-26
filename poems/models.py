from django.db import models
from libs.slughifi import slughifi
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from easy_thumbnails.fields import ThumbnailerImageField


class Poem(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, blank=True)
    body = models.TextField(max_length=99999)
    slug = models.SlugField(max_length=100, blank=True)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # letters = models.IntegerField()
    # lines = models.IntegerField()
    # strophes = models.IntegerField()
    # user = models.ForeignKey('userprofile.User', blank=True, \
    # null=True, on_delete=models.SET_NULL)
    # users = models.ManyToManyField('userprofile.User', blank=True, null=True)
    # tags = models.ManyToManyField('tags.Tag', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.title:
            self.title = self.body[:60]

        self.slug = slughifi(self.title)
        super(Poem, self).save(*args, **kwargs)
