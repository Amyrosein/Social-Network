from django.db import models
from django.conf import settings


class Friendship(models.Model):
	request_from = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='friend_request_from')
	request_to = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='friend_request_to')
	is_accepted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Friendship"
		verbose_name_plural = "Friendships"
		unique_together = ('request_from', 'request_to')
