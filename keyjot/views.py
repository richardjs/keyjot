from django.shortcuts import render

from django.http import HttpResponse

def editor(request, filename):
	return render(request, 'keyjot/editor.html', locals())
