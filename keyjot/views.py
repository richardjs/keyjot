import os

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


@login_required
def editor(request, filename):
	return render(request, 'keyjot/editor.html', locals())

@login_required
def get_data(request, filename):
	user_dir = os.path.join(settings.DATA_DIR, request.user.username)
	if not os.path.exists(user_dir):
		os.makedirs(user_dir)

	full_path = os.path.join(user_dir, filename+'.md')
	if not os.path.exists(full_path):
		open(full_path, 'w').close()
	with open(full_path, 'r') as f:
		data = f.read()

	return HttpResponse(data)

def login_form(request):
	if request.method == 'GET':
		return render(request, 'keyjot/login.html');
	
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is None or not user.is_active:
		return render(request, 'keyjot/login.html');

	login(request, user)
	
	nextPage = ''
	if 'next' in request.GET:
		nextPage = request.GET['next']
	return redirect(nextPage)
