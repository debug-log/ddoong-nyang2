from rest_framework import serializers
from myapp.models.User import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'created_date',)

    def __str__(self):
        return self.name

    def create(self, validated_data):
        return User.objects.create(**validated_data)
