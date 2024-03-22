from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome')
    
    class Meta:
        verbose_name = 'Categoria'
    
    def __str__(self) -> str:
        return f'{self.name}'
class Contact(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=60, blank=True, verbose_name='Sobrenome')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True, verbose_name='E-mail')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de cadastro')
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True, verbose_name='Ativo')
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Foto')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True, 
        verbose_name='Categoria'
        )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True, 
        verbose_name='Responsavel pelo cadastro'
        )
    
    class Meta:
        verbose_name = 'Contato'
        # app_label = ''
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'