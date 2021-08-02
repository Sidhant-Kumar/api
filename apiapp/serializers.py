from rest_framework import serializers
from apiapp.models import apimodel
from rest_framework.serializers import ModelSerializer


class apiserializer(serializers.ModelSerializer):
    class Meta:
        model = apimodel
        fields = '__all__'
