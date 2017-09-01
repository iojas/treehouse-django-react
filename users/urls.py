from django.conf.urls import url, include
from . import views

urlpatterns = [
  url('^dashboard/$', views.dashboard, name = 'dashboard'),
  url('^logout/$', views.LogoutView.as_view(), name='logout'),
  url('^', include('django.contrib.auth.urls')),
]