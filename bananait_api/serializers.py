from dataclasses import fields
from rest_framework import serializers
from banana_web_api.models import person

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'