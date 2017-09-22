
from rest_framework import routers, serializers, viewsets

from .models import *

class ThoughtsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Thoughts
    fields = ('recorded_at','condition','notes')
