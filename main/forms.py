from django import forms
from django.contrib.auth.models import Group
from . import models


class RegistrationForm(forms.Form):
	#
	# form for registration a new user
	#
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	birthday = forms.DateField(
		input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y'),
		required=False,
		)

	def signup(self, request, user):
		# first and last names
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		# set default group 'users' 
		user.groups.add(Group.objects.get(name='users'))
		user.save()
		# store birthday to UserInfo object
		if self.cleaned_data['birthday']:
			user.userinfo.birthday = self.cleaned_data['birthday']
			user.userinfo.save()


class NewsPostForm(forms.ModelForm):
	#
	# form for adding a new post
	#
	class Meta:
		model = models.NewsPost
		fields = ['title', 'text']


class CommentForm(forms.ModelForm):
	#
	# form for posting a comment
	#
	class Meta:
		model = models.Comment
		fields = ['text']