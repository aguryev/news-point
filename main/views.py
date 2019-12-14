from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from django.db.models import Q
from anymail.message import AnymailMessage
from . import models, forms, tasks

# Create your views here.

class AddPostView(CreateView):
	#
	# creates a new post
	#
	model = models.NewsPost
	form_class = forms.NewsPostForm
	template_name = 'add_post.html'
	success_url = '/'

	def form_valid(self, form):
		# add author
		form.instance.author = self.request.user
		# check if premoderation is not required required
		if self.request.user.groups.filter(Q(name='admins')|Q(name='editors')).exists():
			form.instance.status = 1

		return super(AddPostView, self).form_valid(form)


def index(request):
	#
	# shows a list of published posts
	#
	posts = models.NewsPost.objects.filter(status=1).order_by('-posted')
	return render(
			request=request,
			template_name='list_posts.html',
			context={'posts':posts},
			)

def single_post(request, post_id):
	#
	# shows a single post
	#

	# get the current post
	newspost = get_object_or_404(models.NewsPost, id=post_id)

	# check if comment posted
	if request.method == 'POST':
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			# create and save the comment
			comment = models.Comment(
				text = form.cleaned_data.get('text'),
				author = request.user,
				post = newspost,
				)
			comment.save()

			# send mail notification to the post's author
			tasks.send_mail_on_comment.delay(newspost.author.id, newspost.id, request.headers['host'])
	
	# get list of comments to the current post
	comments = models.Comment.objects.filter(post=newspost).order_by('-posted')

	return render(
		request=request,
		template_name='single_post.html',
		context={
			'newspost': newspost,
			'comments': comments,
			'form': forms.CommentForm,
			},
		)
