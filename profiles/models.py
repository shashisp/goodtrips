from __future__ import unicode_literals

from django.db import models
from annoying.fields import AutoOneToOneField


class UserProfile(models.Model):
	user = AutoOneToOneField('auth.user')
	bio = models.TextField()
	profile_pic = models.URLField(null=True)
	access_token = models.CharField(max_length=200, null=True)

	def __unicode__(self):
		return self.user.first_name


def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
	if is_new:
		profile = UserProfile.objects.get_or_create(user=user)[0]
		profile.access_token = response.get('access_token')
		profile.save()
	else:
		profile = UserProfile.objects.get(user=user)
		profile.save()
