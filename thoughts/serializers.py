
from rest_framework import routers, serializers, viewsets

from .models import *

class ThoughtsSerializer(serializers.HyperlinkedModelSerializer):

  condition_display = serializers.SerializerMethodField()

  class Meta:
    model = Thoughts
    fields = ('recorded_at','condition', 'condition_display', 'notes','user')
    read_only_fields = ('recorded_at',)

  def create(self, validated_data):
    thought = Thoughts(**validated_data)
    thought.user = self.context['request'].user
    thought.save()
    return thought

  def get_condition_display(self,obj):
    return obj.get_condition_display()
