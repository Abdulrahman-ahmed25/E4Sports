from rest_framework import serializers
from .models import SportNew

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportNew
        fields = '__all__'


