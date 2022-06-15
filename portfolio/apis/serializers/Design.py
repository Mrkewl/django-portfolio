
from ..models.design import Design
from rest_framework import serializers

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'