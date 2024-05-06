from rest_framework import serializers

from core.models import Runner


class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Runner
        fields=('__all__')