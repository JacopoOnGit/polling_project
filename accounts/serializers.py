from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio']
        extra_kwargs = {
            'password': {'write_only': True},
            'bio': {'required': False},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User()
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        user.set_password(password)
        user.save()
        return user
