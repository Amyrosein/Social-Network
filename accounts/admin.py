from django.contrib import admin

from .models import Profile, Country, Device


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'phone_number', 'country', 'avatar']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ['name', 'abbr', 'is_enabled']


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
	list_display = ['user', 'device_uuid', 'device_type', 'last_login', 'device_os', 'device_model', 'app_version']
