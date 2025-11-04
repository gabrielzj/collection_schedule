from core.models import CollectionCall
# from app.serializers import CollectionCallSerializer
from .serializers import CustomTokenObtainPairSerializer, UserWebSerializer, CollectionCallWebSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError as DRFValidationError

#TODO: criar view para verify token, ou refresh de token, talvez não 
# precise criar um serializer para isso, mas sim usar o serializer do SimpleJWT


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        serializer = UserWebSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except DRFValidationError as e:
        # Retorna os erros de validação de forma estruturada para o frontend exibir naturalmente
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        # Fallback genérico
        return Response({'error': 'Não foi possível concluir o cadastro.'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([AllowAny])
def list_calls(request):
    try:
        calls = CollectionCall.objects.all()
        if not calls.exists():
            return Response({"detail": "Não existem chamadas de coleta para listagem."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CollectionCallWebSerializer(calls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def call_status(request, pk):
    try:
        call = get_object_or_404(CollectionCall, pk=pk)
        serializer = CollectionCallWebSerializer(instance=call, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

