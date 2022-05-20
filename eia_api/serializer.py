from rest_framework import serializers

class DotSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    value=serializers.FloatField()
    units=serializers.CharField()
    devices_id=serializers.IntegerField()