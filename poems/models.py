from django.db import models
from libs.slughifi import slughifi
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
# from easy_thumbnails.fields import ThumbnailerImageField


class Poem(models.Model):

    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=60, blank=True)
    author = models.CharField(max_length=60, blank=True)
    book = models.CharField(max_length=60, blank=True)
    body = models.TextField(max_length=99999)
    slug = models.SlugField(max_length=100, blank=True)
    tags = TaggableManager()
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image_poems', blank=True, null=True)
    # letters = models.IntegerField()
    # lines = models.IntegerField()
    # strophes = models.IntegerField()
    # user = models.ForeignKey('userprofile.User', blank=True, \
    # null=True, on_delete=models.SET_NULL)
    # users = models.ManyToManyField('userprofile.User', blank=True, null=True)
    # tags = models.ManyToManyField('tags.Tag', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poem_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        if not self.title:
            self.title = self.body[:(self.body.index('/') or 60)].strip(',.:;')

        self.slug = slughifi(self.title)
        super(Poem, self).save(*args, **kwargs)

    def get_poem(self):
        return '<p>' + '</p><p>'.join(self.body.split('/')) + '</p>'

    def get_cut_poem(self):
        return '<p>' + '</p><p>'.join(self.body[:min(300, len(self.body)/2)]
                                .split('/')) + '</p><p>...</p>'
