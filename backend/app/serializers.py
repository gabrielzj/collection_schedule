from .models import User, CollectionCall
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                {"password":"A senha deve conter pelo menos 8 caracteres."}
            )
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "O número de telefone deve conter apenas números"
            )
        elif len(value) < 10:
            raise serializers.ValidationError(
                "O número de telefone deve ter pelo menos 10 dígitos."
            )
        return value
    
class CollectionCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCall
        fields = '__all__'
        
    def validade_user(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError(
                {"user": "Usuário vinculado ao chamado não encontrado."}
            )
        return value
    
    def validade_amount_to_collected(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                {"amount_to_collected": "O valor a ser coletado deve ser maior que zero."}
            )
        elif value.isstring():
            raise serializers.ValidationError(
                {"amount_to_collected": "O valor a ser coletado deve ser um número."}
            )
        elif value > 10000:
            raise serializers.ValidationError(
                {"amount_to_collected": "Não é posssível criar um chamado de coleta com essa quantia."}
            )
        return value

