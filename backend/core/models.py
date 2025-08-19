from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_APP = 'app'
    USER_TYPE_WEB = 'web'

    USER_TYPE_CHOICES = [
        (USER_TYPE_APP, 'Aplicativo'),
        (USER_TYPE_WEB, 'Web'),
    ]

    email = models.EmailField(unique=True, null=False, blank=True, default='', verbose_name='Email')
    address = models.CharField(max_length=255, null=True, blank=False, verbose_name='Endereço')
    phone_number = models.CharField(max_length=15, null=True, blank=False, verbose_name='Número de Telefone')
    profile_type = models.CharField(max_length=20, null=False, blank=False, default="app", choices=USER_TYPE_CHOICES, verbose_name='Tipo de usuário',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-id']

    def __str__(self):
        return self.username

class CollectionCall(models.Model):
    URGENCY_LOW = 'low'
    URGENCY_MEDIUM = 'medium'
    URGENCY_HIGH = 'high'

    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'

    URGENCY = [
        (URGENCY_LOW, 'Baixa'),
        (URGENCY_MEDIUM, 'Moderada'),
        (URGENCY_HIGH, 'Alta'),
    ]

    STATUS = [
        (STATUS_PENDING, 'Pendente'),
        (STATUS_COMPLETED, 'Finalizada'),
        (STATUS_FAILED, 'Falha'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_calls',
                             verbose_name='Usuário Responsável')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    amount_to_collected = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor a ser Coletado')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição do Chamado')
    urgency = models.CharField(max_length=50, choices=URGENCY, default=URGENCY_LOW, verbose_name='Urgência do Chamado')
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS_PENDING, verbose_name='Status do Chamado')
    best_time_for_collection = models.DateTimeField(null=True, blank=True, verbose_name='Melhor Horário para Coleta')

    class Meta:
        verbose_name = 'Chamado de Coleta'
        verbose_name_plural = 'Chamados de Coleta'
        ordering = ['-created_at']

    def __str__(self):
        return f"Chamado de coleta criado por {self.user.username}"
