
from rest_framework import routers, serializers, viewsets

from .models import *

class ThoughtsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Thoughts
    fields = ('recorded_at','condition','notes')
    read_only_fields = ('recorded_at',)

  def create(self, validated_data):
    thought = Thoughts(**validated_data)
    thought.user = self.context['request'].user
    thought.save()
    return thought
