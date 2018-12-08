from rest_framework import serializers
from .models import Mumin

class MuminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mumin
        fields = '__all__'