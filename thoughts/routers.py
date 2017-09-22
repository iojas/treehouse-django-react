
from rest_framework import  serializers

from .viewsets import *

router = routers.DefaultRouter()
router.register(r'thoughts', ThoughtsViewSet, base_name = 'thoughts')
