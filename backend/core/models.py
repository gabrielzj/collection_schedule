from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_APP = 'app'
    USER_TYPE_WEB = 'web'

    USER_TYPE_CHOICES = [
        (USER_TYPE_APP, 'Aplicativo'),
        (USER_TYPE_WEB, 'Web'),
    ]

    username = models.CharField(null=True, blank=True, default="", unique=False)
    email = models.EmailField(unique=True, null=False, blank=True, default='', verbose_name='Email')
    address = models.CharField(max_length=255, null=False, blank=False, default='', verbose_name='Endereço')
    phone_number = models.CharField(max_length=20, null=False, blank=False, default='', verbose_name='Número de Telefone')
    profile_type = models.CharField(max_length=20, null=False, blank=False, default="app", choices=USER_TYPE_CHOICES, verbose_name='Tipo de usuário',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

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
    STATUS_UNDER_ANALYSIS = 'in_process'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'
    
    TYPE_PAPER = 'paper'
    TYPE_METAL = 'metal'
    TYPE_PLASTIC = 'plastic'
    TYPE_ELECTRONIC = 'electronic'
    TYPE_ORGANIC = 'organic'
    TYPE_GLASS = 'glass'
    TYPE_RESIDUAL_WASTE = 'residual_waste'
    TYPE_OTHER = 'other'
    
    
    URGENCY = [
        (URGENCY_LOW, 'Baixa'),
        (URGENCY_MEDIUM, 'Moderada'),
        (URGENCY_HIGH, 'Alta'),
    ]

    STATUS = [
        (STATUS_PENDING, 'Pendente'),
        (STATUS_COMPLETED, 'Finalizada'),
        (STATUS_FAILED, 'Cancelada'),
        (STATUS_UNDER_ANALYSIS, 'Em Andamento'),
    ]
    
    TYPES = [
        (TYPE_PAPER, 'Papel'),
        (TYPE_METAL, 'Metal'),
        (TYPE_PLASTIC, 'Plástico'),
        (TYPE_ELECTRONIC, 'Eletrônico'),
        (TYPE_ORGANIC, 'Orgânico'),
        (TYPE_GLASS, 'Vidro'),
        (TYPE_RESIDUAL_WASTE, 'Resíduo Sólido'),
        (TYPE_OTHER, 'Outro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_calls',
                             verbose_name='Usuário Responsável')
    type = models.CharField(blank=False, null=False, choices=TYPES, default=TYPE_OTHER, verbose_name='Tipo de Resíduo')
    address = models.CharField(max_length=255, null=False, blank=False, default='', verbose_name='Endereço')
    amount_to_collect = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor a ser Coletado')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição do Chamado')
    urgency = models.CharField(choices=URGENCY, default=URGENCY_LOW, verbose_name='Urgência do Chamado')
    status = models.CharField(choices=STATUS, default=STATUS_PENDING, verbose_name='Status do Chamado')
    # best_time_for_collection_date = models.DateField(null=True, blank=True, verbose_name='Melhor Data para Coleta')
    # best_time_for_collection_time = models.TimeField(null=True, blank=True, verbose_name='Melhor Horário para Coleta')
    best_time_for_collect = models.DateTimeField(null=True, blank=True, verbose_name='Melhor Data/Horário para Coleta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        verbose_name = 'Chamado de Coleta'
        verbose_name_plural = 'Chamados de Coleta'
        ordering = ['-created_at']

    def __str__(self):
        return f"Chamado de coleta criado por {self.user.username}"
