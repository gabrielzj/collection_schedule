from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import User, CollectionCall
from .serializers import UserSerializer, CollectionCallSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.permissions import AllowAny

#TODO: criar view para verify token, ou refresh de token, talvez não 
# precise criar um serializer para isso, mas sim usar o serializer do SimpleJWT

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def list_users(request):
    try:
        # usar prefetch_related para otimizar consultas ?
        users = User.objects.all()
        if not User.objects.exists():
            raise ValidationError("Não existem usuários para listagem.")
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def retrieve_user(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        if not user:
            raise ValidationError("Usuário com ID informado não existente.")
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Http404:
        return Response(
            {"detail": "Usuário com o ID informado não foi encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def update_user(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if 'password' in serializer.validated_data:
            password = serializer.validated_data.pop('password')
            user.set_password(password)
        
        for  attr, value in serializer.validated_data.items():
            setattr(user, attr, value)
        
        user.save()
        
        response_serializer = UserSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    except Http404:
        return Response(
            {"detail": "Usuário com o ID informado não foi encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'Usuário deletado com sucesso:'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_collection_call(request):
    user_id = request.data.get('user')
    
    if not user_id:
        return Response(
            {'error': 'É obrigatório informar um usuário para criar um chamado de coleta.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if not User.objects.filter(id=user_id).exists():
        return Response(
            {'error': 'Usuário com o ID informado não foi encontrado.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    try:
        serializer = CollectionCallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def list_collection_call(request):
    try:
        collection_calls = CollectionCall.objects.all().order_by('-created_at')
        serializer = CollectionCallSerializer(collection_calls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def retrieve_collection_call(request, pk):
    try:
        collection_call = get_object_or_404(CollectionCall, pk=pk)
        user = CollectionCall.objects.filter(user_id=collection_call.user_id).exists()
        if not user:
            raise ValidationError({'collection_calls': 'Chamado sem usuário vinculado'})
        serializer = CollectionCallSerializer(collection_call)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Http404:
        return Response(
            {"detail": "Chamado com ID informado não foi encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def update_collection_call(request, pk):
    try:
        collection_call = get_object_or_404(CollectionCall, pk=pk)
        serializer = CollectionCallSerializer(collection_call, data=request.data, partial=True)
        user = request.data.get('user')
        if user:
            if not CollectionCall.objects.filter(user_id=user).exists():
                return Response({'collection_calls': 'Usuário vinculado ao chamado inexistente'}, status=status.HTTP_404_NOT_FOUND)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Http404:
        return Response(
            {"detail": "Chamado com o ID informado não foi encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_collection_call(request, pk):
    try:
        collection_call = get_object_or_404(CollectionCall, pk=pk)
        collection_call.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Http404:
        return Response(
            {"detail": "Chamado com ID informado não foi encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)