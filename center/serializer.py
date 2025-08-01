from rest_framework import serializers
from .models import Oquv_markaz

class Oquv_markazSerializer(serializers.ModelSerializer):

    class Meta:
        model = Oquv_markaz
        fields = "__all__"
