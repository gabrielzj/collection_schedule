from core.models import User, CollectionCall
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
import numbers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    class Meta:
        ref_name = 'AppCustomTokenObtainPairSerializer'

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if not user.is_active:
            raise AuthenticationFailed('Usuário Inativo')
        if user.profile_type != User.USER_TYPE_APP:
            raise AuthenticationFailed('Tipo de usuário inválido.')
        
        return data

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
    
    def validate_profile_type(self, value):
        if value != User.USER_TYPE_APP:
            raise serializers.ValidationError(
                'Tipo de perfil inválido'
            )
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CollectionCallSerializer(serializers.ModelSerializer):
    # relação entre models
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.ChoiceField(
        choices=CollectionCall.TYPES,
        error_messages={
            'invalid_choice': 'Informe um tipo de resíduo válido.',
        }
    )
    address = serializers.CharField(
        error_messages={
            'blank': 'O campo endereço não pode estar vazio.',
        }
    )
    
    class Meta:
        model = CollectionCall
        fields = '__all__'
    
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     if request and request.user and request.user.is_authenticated:
    #         validated_data['user'] = request.user
    #     return super().create(validated_data)
    
    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError({"address": "Campo obrigatório."})
        return value

    def validate_amount_to_collected(self, value):
        if value is None:
            raise serializers.ValidationError({"amount_to_collected": "Campo obrigatório."})
        if value <= 0:
            raise serializers.ValidationError(
                {"amount_to_collected": "O valor a ser coletado deve ser maior que zero."}
            )
        elif not isinstance(value, numbers.Number):
            raise serializers.ValidationError(
                {"amount_to_collected": "O valor a ser coletado deve ser um número."}
            )
        elif value > 10000:
            raise serializers.ValidationError(
                {"amount_to_collected": "Não é posssível criar um chamado de coleta com essa quantia."}
            )
        return value        

