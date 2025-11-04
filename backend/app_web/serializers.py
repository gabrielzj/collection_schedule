from core.models import User, CollectionCall
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from django.contrib.auth.base_user import BaseUserManager
import logging

logger = logging.getLogger(__name__)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    class Meta:
        ref_name = 'WebCustomTokenObtainPairSerializer'

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        
        if not user.is_active:
            raise AuthenticationFailed("Usuário inativo.")
        if user.profile_type != User.USER_TYPE_WEB:
            raise AuthenticationFailed("Tipo de usuário inválido.")

        return data
    
class UserWebSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=False)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'address']

    def validate_profile_type(self, value):
        if value != User.USER_TYPE_WEB:
            raise serializers.ValidationError("Tipo de perfil inválido.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve conter pelo menos 8 caracteres.")
        return value
    
    def create(self, validated_data):
        # Força o tipo de perfil como WEB e garante hashing de senha e normalização do email
        raw_password = validated_data.pop('password', None)

        email = BaseUserManager.normalize_email(validated_data.get('email', ''))
        validated_data['email'] = email

        # Garante que o usuário criado aqui sempre seja do tipo WEB
        validated_data['profile_type'] = User.USER_TYPE_WEB

        user = User(**validated_data)
        if raw_password:
            user.set_password(raw_password)
        else:
            user.set_unusable_password()
        user.save()
        return user
    
class CollectionCallWebSerializer(serializers.ModelSerializer):
    user = UserWebSerializer()
    
    class Meta:
        model = CollectionCall
        fields = ['id', 'type', 'address', 'amount_to_collect', 'description', 'urgency', 'status', 
                  'best_time_for_collect', 'user']