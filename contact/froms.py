from typing import Any, Mapping

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
  # first_name = forms.CharField(
  #   widget = forms.TextInput(
  #     attrs = {
  #       'placeholder': 'teste de escrita',
  #     },
  #   ),
  #   label= 'Primeiro Nome:',
  #   help_text= 'Digite o primeiro nome do contato',
  # )
  
  picture = forms.ImageField(
    widget = forms.FileInput(
      attrs = {
        'aceept': 'image/*'
      }
    ),
    label = 'Foto',
    required = False
  )
     
  class Meta:
    model = Contact
    fields = (
      'first_name', 
      'last_name',
      'phone',
      'email',
      'description',
      'picture',
      'category',             
    )    
    
  def clean(self):
      cleaned_data = self.cleaned_data
      first_name = cleaned_data.get('first_name')
      last_name = cleaned_data.get('last_name')

      if first_name == last_name:
        msg = ValidationError(
          'Primeiro nome não pode ser igual ao segundo',
          code='invalid'
        )
        self.add_error('first_name', msg)
        self.add_error('last_name', msg)

      return super().clean()
  
  def clean_first_name(self):
      first_name = self.cleaned_data.get('first_name')

      if first_name == 'ABC':
        self.add_error(
          'first_name',
          ValidationError(
            'Veio do add_error',
            code='invalid'
          )
        )

      return first_name
      
class RegisterForm(UserCreationForm):
  first_name = forms.CharField(
    required = True,
    label = 'Primeiro nome',    
  )
  
  last_name = forms.CharField(
    required = True,
    label = 'Último nome',
  )
  
  email = forms.EmailField(
    required = True,
    label = 'E-mail',
  )
  
  class Meta:
    model = User
    fields = (
      'first_name', 
      'last_name', 
      'email',
      'username',
      'password1',
      'password2',  
    )
    
  def clean_email(self):
    email = self.cleaned_data.get('email')
    
    if User.objects.filter(email=email).exists():
      self.add_error(
        'email',
        ValidationError(
          'Já existe este "E-mail"',
          code = 'invalid'
        )
      )
    
    return email
  
class RegisterUpdateForm(forms.ModelForm):
  first_name = forms.CharField(
    min_length = 2,
    max_length = 30,
    required = True,
    help_text = 'Obrigatorio.',
    error_messages = {
      'min_length': 'Por favor, adicione mais de 2 letras.'
    },
    label = 'Primeiro nome',
  )
  
  last_name = forms.CharField(
    min_length =2,
    max_length =30,
    required =True,
    help_text ='Obrigatorio.',
    label = 'Último nome',
  )

  password1 = forms.CharField(
    label = "Senha",
    strip = False,
    widget = forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text = password_validation.password_validators_help_text_html(),
    required = False,
  )

  password2 = forms.CharField(
    label="Confirme a senha",
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text='Use a mesma senha de antes.',
    required=False,
  )

  class Meta:
    model = User
    fields = (
      'first_name', 'last_name', 'email',
      'username',
    )

  def save(self, commit=True):
    cleaned_data = self.cleaned_data
    user = super().save(commit=False)
    password = cleaned_data.get('password1')

    if password:
      user.set_password(password)

    if commit:
      user.save()

    return user

  def clean(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

    if password1 or password2:
      if password1 != password2:
        self.add_error(
          'password2',
          ValidationError('Senhas devem identicas.')
        )

    return super().clean()

  def clean_email(self):
    email = self.cleaned_data.get('email')
    current_email = self.instance.email

    if current_email != email:
      if User.objects.filter(email=email).exists():
        self.add_error(
          'email',
          ValidationError('Já existe este e-mail', code='invalid')
        )

    return email

  def clean_password1(self):
    password1 = self.cleaned_data.get('password1')

    if password1:
      try:
        password_validation.validate_password(password1)
      except ValidationError as errors:
        self.add_error(
        'password1',
        ValidationError(errors)
        )

    return password1