from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
