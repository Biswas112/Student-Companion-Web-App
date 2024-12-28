from .models import notes
from .serilizers import NotesSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

class NotesViewSet(ModelViewSet):
  queryset=notes.objects.all()
  serializer_class=NotesSerializer

  
