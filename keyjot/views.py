from django.shortcuts import render

from django.http import HttpResponse

def test(request):
	return render(request, 'keyjot/editor.html')
