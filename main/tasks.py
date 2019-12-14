from . import models
from anymail.message import AnymailMessage
from django.contrib.auth.models import User
from news_point.celery import app

# tasks for celery

@app.task
def send_mail_on_comment(user_id, post_id, host):
	#
	# sends mail on comment post
	#
	user = User.objects.get(id=user_id)
	post = models.NewsPost.objects.get(id=post_id)

	msg = AnymailMessage(
		subject = 'News Point - new comment',
		body = '''
		You have a new comment on post "{}"
		View at {}/post/{}/
		'''.format(post.title, host, post_id),
		to = [user.email],
		)
	msg.send()