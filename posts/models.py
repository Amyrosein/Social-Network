from django.db import models
from django.conf import settings


class Post(models.Model):
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	caption = models.TextField(max_length=512)
	is_active = models.BooleanField(default=True)
	is_public = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title


class PostFile(models.Model):
	post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
	file = models.FileField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Post File'
		verbose_name_plural = "Post Files"

	def __str__(self):
		return f"{self.post}: {self.file}"


class Comment(models.Model):
	post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField(max_length=256)
	is_approved = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'


class Like(models.Model):
	post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='likes')
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_liked = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Like'
		verbose_name_plural = 'Likes'
