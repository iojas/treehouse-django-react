from django.conf.urls import url, include
from . import views

urlpatterns = [
  url('^dashboard/$', views.dashboard.as_view(), name = 'dashboard'),
  url('^logout/$', views.LogoutView.as_view(), name='logout'),
  url('^signup/$', views.SignUpView.as_view(), name='signup'),
  url('^', include('django.contrib.auth.urls')),

]
