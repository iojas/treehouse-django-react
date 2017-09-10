import datetime
from django.conf.urls import url
from django.utils import timezone
from . import views

urlpatterns=[
		url(r'^create/$', views.CreateThoughts.as_view(), name= 'create'),
]