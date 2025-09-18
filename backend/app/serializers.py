from core.models import User, CollectionCall
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.exceptions import AuthenticationFailed
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
        fields = '__all__'
        
    
    def update(self, instance, validated_data):
        # remove password para n passar em texto plano
        password = validated_data.pop('password', None)
        
        for field in ['email', 'address', 'phone_number', 'first_name', 'last_name']:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
                
        if password:
            instance.set_password(password)
            print(instance.set_password(password))
        
        instance.save()
        return instance
    
    def validate_profile_type(self, value):
        if value != User.USER_TYPE_APP:
            raise serializers.ValidationError(
                'Tipo de perfil inválido'
            )
        return value

    # remove a senha do validated_data para que seja tratada separadamente
    def create(self, validated_data):
        password = validated_data.pop('password')
        user =  User.objects.create_user(password=password, **validated_data)
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
    
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     if request and request.user and request.user.is_authenticated:
    #         validated_data['user'] = request.user
    #     return super().create(validated_data)
    
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

