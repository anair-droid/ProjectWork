from rest_framework import serializers

from .models import rpaserverConfig

class rpaServerserializer(serializers.ModelSerializer):
    class Meta:
        model = rpaserverConfig
        fields = ('applob','appname','appUrl','appAPIkey','param')

