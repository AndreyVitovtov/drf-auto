from rest_framework import serializers

from . import models


class SerializedAuto(serializers.ModelSerializer):
    class Meta:
        model = models.Auto
        fields = ['id', 'label', 'year', 'price', 'description']


class SerializedOwner(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = ['first_name', 'last_name']


class SerializedAutosPassport(serializers.ModelSerializer):
    class Meta:
        model = models.AutosPassport
        fields = ['related_auto', 'number', 'prefix']
