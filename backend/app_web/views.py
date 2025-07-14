from core.models import User, CollectionCall
from app.serializers import CollectionCallSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def list_calls(request):
    try:
        calls = CollectionCall.objects.all()
        if not calls.exists():
            return Response({"detail": "Não existem chamadas de coleta para listagem."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CollectionCallSerializer(calls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

