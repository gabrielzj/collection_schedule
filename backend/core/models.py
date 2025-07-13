from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=True, default='', verbose_name='Email')
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    phone_number = models.CharField(max_length=15, null=False, blank=False, verbose_name='Número de Telefone')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-id']

    def __str__(self):
        return self.username


class CollectionCall(models.Model):
    CHOICES_URGENCY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_calls',
                             verbose_name='Usuário Responsável')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount_to_collected = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    urgency = models.CharField(max_length=50, choices=CHOICES_URGENCY, default='low')
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    best_time_for_collection = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Chamado de Coleta'
        verbose_name_plural = 'Chamados de Coleta'
        ordering = ['-created_at']

    def __str__(self):
        return f"Chamado de coleta criado por {self.user.username}"
