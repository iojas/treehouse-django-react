"""feelings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings

from django.views.generic import TemplateView

from thoughts import urls as thoughts_url
from users import urls as user_urls
from groups import urls as groups_urls
# from thoughts.view import DashboardView
from rest_framework_jwt.views import obtain_jwt_token

from users import routers as user_router
from thoughts import routers as thought_router

api_urlpatterns = [
    url(r'',include(user_router.router.urls)),
    url(r'',include(thought_router.router.urls)),

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(user_urls, namespace = 'users')),
    url(r'^thought/', include(thoughts_url, namespace='thoughts')),
    url(r'^groups/', include(groups_urls, namespace = 'groups')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name= 'home'),
    url(r'^api/', include(api_urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
