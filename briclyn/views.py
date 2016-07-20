from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext

from .models import *
from briclyn.forms import *



def index(request):
	return render(request, 'official/index.html', {})


def edit_profile(request):

	user = request.user
	profile = UserProfile.objects.filter(user=user).get()
	user_form = UserForm(request.POST, instance=user)
	profile_form = ProfileForm(request.POST, instance=profile)

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, instance=profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save(commit=False)
			profile_form.save(commit=False)
			return HttpResponseRedirect('/home')
		else:
			form.ValidationError("Invalid details provided")
	else:
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, instance=profile)
	return render(request, 'official/profile.html', {'user_form':user_form, 'profile_form':profile_form})