from .models import CollectionCall, User
from .serializers import UserSerializer, CollectionCallSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

#TODO: implementar as views do user
#TODO: implementar validação de user em outras views
class CollectionCallCreateView(generics.CreateAPIView):
    serializer_class = CollectionCallSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')
        
        if not user:
            # return Response({'detail': 'Não é possível criar um chamado de coleta sem um usuário vinculado.'}, status=status.HTTP_400_BAD_REQUEST)
            raise ValidationError({'user:': 'Não é possível criar um chamado de coleta sem um usuário vinculado.'})
        
        if not User.objects.filter(id=user).exists():
            raise ValidationError({'user': 'Usuário vinculado ao chamado não encontrado.'})
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # chama o save, padrão do CreateAPIView
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CollectionCallListView(generics.ListAPIView):
    serializer_class = CollectionCallSerializer
     
    # retorna a queryset da view
    def get_queryset(self):
        queryset = CollectionCall.objects.filter(user=self.request.user)
        return queryset.order_by('-created_at')
    
class CollectionCallRetrieveView(generics.RetrieveAPIView):
    serializer_class = CollectionCallSerializer
    
    # por trás chama o get_object passando self.kwargs['pk'] da URL
    def get_queryset(self):
        queryset = CollectionCall.objects.filter(user=self.request.user)
        return queryset
    
class CollectionCallDeleteView(generics.DestroyAPIView):
    serializer_class = CollectionCallSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response('Chamado deletado com sucesso', status=status.HTTP_204_NO_CONTENT)
    
    
    
    
