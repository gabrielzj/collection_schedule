from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    
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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_calls', verbose_name='Usuário Responsável') 
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