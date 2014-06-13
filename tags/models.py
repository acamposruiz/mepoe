from django.db import models
from libs.slughifi import slughifi
# from easy_thumbnails.fields import ThumbnailerImageField

class Tag(models.Model):

	name = models.CharField(max_length=60)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=100)
	parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	vid = models.ForeignKey('Vocabulary', blank=True, null=True, on_delete=models.SET_NULL)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
	    self.slug = slughifi(self.name)
	    super(Tag, self).save(*args, **kwargs)


class Vocabulary(models.Model):

	name = models.CharField(max_length=60)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=100)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
	    self.slug = slughifi(self.name)
	    super(Vocabulary, self).save(*args, **kwargs)