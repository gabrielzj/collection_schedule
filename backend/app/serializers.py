from core.models import User, CollectionCall
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.base_user import BaseUserManager
import numbers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    class Meta:
        ref_name = 'AppCustomTokenObtainPairSerializer'

    def validate(self, attrs):
        data = super().validate(attrs)
        # usuário atual já autenticado
        user = self.user
        id = user.id
        data['id'] = id

        if not user.is_active:
            raise AuthenticationFailed('Usuário Inativo')
        if user.profile_type != User.USER_TYPE_APP:
            raise AuthenticationFailed('Tipo de usuário inválido.')
        
        return data
    
class CustomRefreshTokenSerializer(TokenRefreshSerializer):
    class Meta:
        ref_name = 'AppCustomRefreshTokenSerializer'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=False)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'address', 'phone_number', 'profile_type']
        
    
    def update(self, instance, validated_data):
        # remove password para n passar em texto plano
        password = validated_data.pop('password', None)
        
        for field in ['email', 'address', 'phone_number', 'first_name', 'last_name']:
            if field in validated_data:
                # set instance.field como validated_data[field]
                setattr(instance, field, validated_data[field])
                
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance
    
    def validate_profile_type(self, value):
        if value != User.USER_TYPE_APP:
            raise serializers.ValidationError(
                'Tipo de perfil inválido'
            )
        return value

    def create(self, validated_data):
        # remove a senha para transformar em hash com set_password
        raw_password = validated_data.pop('password', None)
        
        # padroniza emails
        email = BaseUserManager.normalize_email(validated_data.get('email', ''))
        validated_data['email'] = email
        
        user = User(**validated_data)
        
        if raw_password:
            user.set_password(raw_password)
        else:
            user.set_unusable_password()
        
        user.save()
        return user
    
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
    
    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError({"address": "Campo obrigatório."})
        return value

    def validate_amount_to_collect(self, value):
        if value is None:
            raise serializers.ValidationError({"amount_to_collect": "Campo obrigatório."})
        if value <= 0:
            raise serializers.ValidationError(
                {"amount_to_collect": "O valor a ser coletado deve ser maior que zero."}
            )
        elif not isinstance(value, numbers.Number):
            raise serializers.ValidationError(
                {"amount_to_collect": "O valor a ser coletado deve ser um número."}
            )
        elif value > 10000:
            raise serializers.ValidationError(
                {"amount_to_collect": "Não é posssível criar um chamado de coleta com essa quantia."}
            )
        return value
    
    def validate_best_time_for_collect(self, value):
        if value:
            from django.utils import timezone
            if value < timezone.now():
                raise serializers.ValidationError(
                    {"best_time_for_collect": "O melhor horário para coleta não pode ser no passado."}
                )       
        return value
