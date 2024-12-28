from rest_framework import serializers
from . models import notes
from django.contrib.auth.models import User

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=notes
        fields="__all__"
