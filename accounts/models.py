from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
	name = models.CharField(max_length=50)
	abbr = models.CharField(max_length=5)
	is_enabled = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Country'
		db_table = 'countries'


class Profile(models.Model):
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
	country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
	avatar = models.ImageField(blank=True)


class Device(models.Model):
	DEVICE_WEB = 1
	DEVICE_IOS = 2
	DEVICE_ANDROID = 3
	DEVICE_PC = 4
	DEVICE_TYPES_CHOICES = (
		(DEVICE_WEB, 'web'),
		(DEVICE_IOS, 'ios'),
		(DEVICE_ANDROID, 'android'),
		(DEVICE_PC, 'pc')
	)

	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
	device_uuid = models.UUIDField('device uuid', null=True)
	last_login = models.DateTimeField('last login date', null=True)
	device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPES_CHOICES, default=DEVICE_WEB)
	device_os = models.CharField('device os', max_length=20, blank=True)
	device_model = models.CharField('device model', max_length=50, blank=True)
	app_version = models.CharField('app version', max_length=20, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'user_devices'
		verbose_name = _('device')
		verbose_name_plural = _('devices')
		unique_together = ('user', 'device_uuid')
