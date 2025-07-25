# Generated by Django 5.2.3 on 2025-07-14 19:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True, verbose_name='Email')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Endereço')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Número de Telefone')),
                ('profile_type', models.CharField(choices=[('app', 'Aplicativo'), ('web', 'Web')], max_length=20, verbose_name='Tipo de usuário')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CollectionCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('amount_to_collected', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor a ser Coletado')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição do Chamado')),
                ('urgency', models.CharField(choices=[('low', 'Baixa'), ('medium', 'Moderada'), ('high', 'Alta')], default='low', max_length=50, verbose_name='Urgência do Chamado')),
                ('status', models.CharField(choices=[('pending', 'Pendente'), ('completed', 'Finalizada'), ('failed', 'Falha')], default='pending', max_length=50, verbose_name='Status do Chamado')),
                ('best_time_for_collection', models.DateTimeField(blank=True, null=True, verbose_name='Melhor Horário para Coleta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_calls', to=settings.AUTH_USER_MODEL, verbose_name='Usuário Responsável')),
            ],
            options={
                'verbose_name': 'Chamado de Coleta',
                'verbose_name_plural': 'Chamados de Coleta',
                'ordering': ['-created_at'],
            },
        ),
    ]
