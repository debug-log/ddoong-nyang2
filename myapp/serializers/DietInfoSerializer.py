from rest_framework import serializers
from myapp.models.DietInfo import DietInfo

class DietInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietInfo
        fields = ('text', 'types', 'photo_url', 'button_label', 'button_url', 'date')

    def __str__(self):
        return self.button_label

    def create(self, validated_data):
        return DietInfo.objects.create(**validated_data)
