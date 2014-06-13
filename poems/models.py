from django.db import models
from libs.slughifi import slughifi
# from easy_thumbnails.fields import ThumbnailerImageField

class Poem(models.Model):

	title = models.CharField(max_length=60, blank=True, null=True)
	body = models.TextField()
	# user = models.ForeignKey('userprofile.User', blank=True, null=True, on_delete=models.SET_NULL)
	# users = models.ManyToManyField('userprofile.User', blank=True, null=True)
	tags = models.ManyToManyField('tags.Tag', blank=True, null=True)
	slug = models.SlugField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):

		if not self.title:
			self.title = self.body[:60]

		self.slug = slughifi(self.title)
		super(Poem, self).save(*args, **kwargs)
	    

	    
