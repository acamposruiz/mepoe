from django.db import models
# from easy_thumbnails.fields import ThumbnailerImageField

class Poem(models.Model):

	title = models.CharField(max_length=60)
	body = models.TextField()
	user = models.ForeignKey('userprofile.User', blank=True, null=True, on_delete=models.SET_NULL)
	users = models.ManyToManyField('userprofile.User', blank=True, null=True, on_delete=models.SET_NULL)
	tags = models.ManyToManyField('tags.Tag', blank=True, null=True, on_delete=models.SET_NULL)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
