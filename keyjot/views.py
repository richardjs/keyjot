import os

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Help function -- not a web view
def get_file(username, filename, mode='r'):
	user_dir = os.path.join(settings.DATA_DIR, username)
	if not os.path.exists(user_dir):
		os.makedirs(user_dir)

	full_path = os.path.join(user_dir, filename+'.md')
	if not os.path.exists(full_path):
		open(full_path, 'w').close()
	return open(full_path, mode)

@login_required
def editor(request, filename):
	return render(request, 'keyjot/editor.html', locals())

@login_required
def get_data(request, filename):
	with get_file(request.user.username, filename) as f:
		data = f.read()
	return HttpResponse(data)

@login_required
def save_data(request, filename):
	data = request.POST['data']
	with get_file(request.user.username, filename, 'w') as f:
		f.write(data)
	return HttpResponse('ok')

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
