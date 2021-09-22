from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.forms import ValidationError
import re
from utils import validator
from django import forms

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='User')
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30, blank=True)
    neighbourhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.user}'

    def clean(self):
        error_messages = {}

        if not validator.CPF_validate(self.cpf):
            error_messages['cpf'] = 'CPF invalid.'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) != 8:
            error_messages['cep'] = 'Invalid CEP, insert just the 8 digits.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'