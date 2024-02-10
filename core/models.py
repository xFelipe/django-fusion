import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_name(_instance, filename):
    """Returns a new name for the uploaded file."""
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return new_filename


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField('Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Ícone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class Role(Base):
    role = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.role


class Employee(Base):
    name = models.CharField('Nome', max_length=100)
    role = models.ForeignKey('core.Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Imagem',
                           upload_to=get_file_name,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.URLField('Facebook', max_length=100, default='#')
    twitter = models.URLField('Twitter', max_length=100, default='#')
    instagram = models.URLField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name
