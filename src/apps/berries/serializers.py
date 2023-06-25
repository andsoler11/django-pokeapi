from rest_framework import serializers
from apps.berries.models import Berrie

class BerrieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berrie
        fields = '__all__'