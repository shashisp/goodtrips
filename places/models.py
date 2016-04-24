from __future__ import unicode_literals

from django.db import models
from profiles.models import UserProfile
from utils import analyze_text, querytext_index


class Place(models.Model):
	name = models.CharField(max_length=250)
	latitiude = models.FloatField()
	longitude = models.FloatField()
	description = models.TextField()
	thumbnail = models.URLField()
	extra_data = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

	def get_all_feedbacks(self):
		return self.feedbacks.all().values('description', 'given_by__profile_pic', 'given_by__user__first_name', 'given_by', 'is_postive')

	def save(self, *args, **kwargs):
		self.extra_data = querytext_index(self.name)
		super(Place, self).save(*args, **kwargs)


class Feedback(models.Model):
	place = models.ForeignKey(Place, related_name='feedbacks')
	description = models.TextField()
	is_postive = models.BooleanField(default=None)
	given_by = models.ForeignKey(UserProfile)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		return self.place.name

	def save(self, *args, **kwargs):
		if analyze_text(self.description) < 0:
			self.is_postive = False
		else:
			self.is_postive = True
		super(Feedback, self).save(*args, **kwargs)


class WishList(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='wishlists')
	place = models.ManyToManyField(Place)

	def __unicode__(self):
		return self.created_by.user.first_name