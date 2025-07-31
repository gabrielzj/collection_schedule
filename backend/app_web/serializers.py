from core.models import User, CollectionCall
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
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
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile_type']

    def validate_profile_type(self, value):
        if value != User.USER_TYPE_WEB:
            raise serializers.ValidationError("Tipo de perfil inválido.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve conter pelo menos 8 caracteres.")
        return value
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)