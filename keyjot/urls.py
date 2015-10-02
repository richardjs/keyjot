from django.conf.urls import include, url
from django.contrib import admin

import keyjot.views

urlpatterns = [
	url(r'^$', keyjot.views.test)
]
