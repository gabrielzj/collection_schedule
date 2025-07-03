from .models import CollectionCall, User
from .serializers import UserSerializer, CollectionCallSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

#TODO: implementar as views do user
#TODO: implementar validação de user em outras views
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return User.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().order_by('-id')

class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return User.objects.all()
    
class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return User.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response('Usuário deletado com sucesso', status=status.HTTP_204_NO_CONTENT)


class CollectionCallCreateView(generics.CreateAPIView):
    serializer_class = CollectionCallSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')
        
        if not user:
            raise ValidationError({'user': 'Não é possível criar um chamado de coleta sem um usuário vinculado.'})
        
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
        # queryset = CollectionCall.objects.filter(user=self.request.user)
        queryset = CollectionCall.objects.all().order_by('-created_at')
        return queryset
    
class CollectionCallRetrieveView(generics.RetrieveAPIView):
    serializer_class = CollectionCallSerializer
    lookup_field = 'pk'
    
    # por trás chama o get_object passando self.kwargs['pk'] da URL
    def get_queryset(self):
        # queryset = CollectionCall.objects.filter(user=self.request.user)
        queryset = CollectionCall.objects.all()
        return queryset
    
class CollectionCallUpdateView(generics.UpdateAPIView):
    serializer_class = CollectionCallSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        # queryset = CollectionCall.objects.filter(user=self.request.user)
        queryset = CollectionCall.objects.all()
        return queryset
    
    def update(self, request, *args, **kwargs):
        user = request.data.get('user')
        
        if not user:
            raise ValidationError({'user': 'Não é possível atualizar um chamado de coleta sem um usuário vinculado.'})
        
        if not User.objects.filter(id=user).exists():
            raise ValidationError({'user': 'Usuário vinculado ao chamado não encontrado.'})
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CollectionCallDeleteView(generics.DestroyAPIView):
    serializer_class = CollectionCallSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return CollectionCall.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response('Chamado deletado com sucesso', status=status.HTTP_204_NO_CONTENT)
    
    
    
    
