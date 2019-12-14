from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class NewsPost(models.Model):
	#
	# a news post object
	#
	title = models.CharField(max_length=100)
	text = HTMLField() # reach text tinymce field 
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	posted = models.DateTimeField(default=timezone.now)
	# status of the post
	status = models.IntegerField(default=0, choices=(
		(0, 'Unpublished'),
		(1, 'Published'),
		(2, 'Declined'),
		))

	def __str__(self):
		return ' '.join((
			self.posted.strftime('%d.%m.%Y %H:%m'),
			self.title,
			))

class Comment(models.Model):
	#
	# a comment to a post object
	#
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	posted = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)

	def __str__(self):
		return ' '.join((
			self.posted.strftime('%d.%m.%Y %H:%m'),
			self.post.title,
			))

class UserInfo(models.Model):
	#
	# extension to the User to store birthday
	#
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birthday = models.DateField(default=date.today)

	def __str__(self):
		return self.user.email

# auto creation of the UserInfo object when a User is created
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
	if created:
		UserInfo.objects.create(user=instance)