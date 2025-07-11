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
        try:
            password = validated_data.pop('password')
            user = User()
            if 'bio' in validated_data:
                user.bio = validated_data['bio']
            if 'username' in validated_data:
                user.username = validated_data['username']
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print("Errore nella creazione utente:", e)
            raise serializers.ValidationError("Errore durante la registrazione.")

