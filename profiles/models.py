from __future__ import unicode_literals

from django.db import models
from annoying.fields import AutoOneToOneField


class UserProfile(models.Model):
	user = AutoOneToOneField('auth.user')
	bio = models.TextField()

	def __unicode__(self):
		return self.user.first_name
