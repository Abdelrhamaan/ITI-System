from rest_framework import routers, serializers, viewsets
from .models import *
from django.db.models import fields


# we will point to models in database by serializers
class TraineeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'name']
