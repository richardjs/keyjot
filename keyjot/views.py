import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def editor(request, filename):
	return render(request, 'keyjot/editor.html', locals())

def get_data(request, filename):
	user_dir = os.path.join(settings.DATA_DIR, 'testuser')
	if not os.path.exists(user_dir):
		os.makedirs(user_dir)

	full_path = os.path.join(user_dir, filename+'.md')
	if not os.path.exists(full_path):
		open(full_path, 'w').close()
	with open(full_path, 'r') as f:
		data = f.read()

	return HttpResponse(data)
