from __future__ import unicode_literals

from django.db import models
from profiles.models import UserProfile


class Place(models.Model):
	name = models.CharField(max_length=250)
	latitiude = models.FloatField()
	longitude = models.FloatField()
	description = models.TextField()
	thumbnail = models.URLField()

	def __unicode__(self):
		return self.name


class Feedback(models.Model):
	place = models.ForeignKey(Place, related_name='places')
	description = models.TextField()
	is_postive = models.BooleanField(default=None)
	given_by = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.place.name