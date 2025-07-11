from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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
            # ✅ valida la password secondo le regole Django
            validate_password(password)

            # ✅ crea l'istanza direttamente con i dati restanti
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        except Exception as e:
            print("Errore nella creazione utente:", e)
            raise serializers.ValidationError("Errore durante la registrazione.")