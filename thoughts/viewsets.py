
from rest_framework import  viewsets

from .serializers import *

class ThoughtsViewSet(viewsets.ModelViewSet):
  serializer_class = ThoughtsSerializer

  def get_queryset(self):
    return self.request.user.thoughts.all()

  # def create(self, request, *args, **kwargs):
  #   import pdb; pdb.set_trace()
  #   return super(ThoughtsSerializer, self).create(request, *args, **kwargs)
