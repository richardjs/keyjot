from django.conf.urls import include, url
from django.contrib import admin

import keyjot.views

urlpatterns = [
	url(r'^login$', keyjot.views.login),
	url(r'^(\w+)/get$', keyjot.views.get_data),
	url(r'^(\w+)$', keyjot.views.editor),
]
