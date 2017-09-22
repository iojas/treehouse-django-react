
from rest_framework import  viewsets

from .serializers import *

class ThoughtsViewSet(viewsets.ModelViewSet):
  serializer_class = ThoughtsSerializer

  def get_queryset(self):
    return self.request.user.thoughts.all()
