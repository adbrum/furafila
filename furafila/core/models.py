from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Counter(models.Model):  # Contador
    set = models.CharField('Prefixo', max_length=1)
    total = models.IntegerField('Total', validators=[MaxValueValidator(999)])

    class Meta:
        verbose_name_plural = 'Contadores'
        verbose_name = 'Contador'

    def __str__(self):
        return self.set


class Attendance(models.Model):  # Atendimento
    user = models.OneToOneField(User)
    service = models.ForeignKey('Service')
    priority = models.ForeignKey('Priority')
    accesspoint = models.ForeignKey('AccessPoint')
    ticket = models.CharField('Senha', max_length=4)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    check_in = models.DateTimeField('Entrada', auto_now=True)
    check_out = models.DateTimeField('Saida', null=True)


class Position(models.Model):  # Cargos
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=255)

    class Meta:
        verbose_name_plural = 'Cargos'
        verbose_name = 'Cargo'
        ordering = ('name',)

    def __str__(self):
        return self.name


class AccessPoint(models.Model):  # Ponto de Acesso
    name = models.CharField('Nome', max_length=100)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Pontos de acesso'
        verbose_name = 'Ponto de acesso'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Priority(models.Model):  # Prioridade
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=255)
    priority = models.IntegerField()
    state = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Prioridades'
        verbose_name = 'Prioridade'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Service(models.Model):  # Serviços
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=255)
    template = models.CharField('Template', max_length=100)
    state = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Serviços'
        verbose_name = 'Serviço'
        ordering = ('name',)

    def __str__(self):
        return self.name

# class Group(models.Model):
#     name = models.CharField('Nome', max_length=100)
#     description = models.TextField('Descrição', max_length=255)


# class HistoryService(models.Model):
#     attendance = models.ForeignKey('Attendance')
#     user = models.ForeignKey(User)
#     service = models.ForeignKey('Service')
#     priority = models.ForeignKey('Priority')
#     accesspoint = models.ForeignKey('AccessPoint')
#     created_at = models.DateTimeField('criado em', auto_now_add=True)
#     check_in = models.DateTimeField('entrada', auto_now=True)
#     check_out = models.DateTimeField('saida', null=True)
#     status = models.CharField('Estado', max_length=50)
#     ticket = models.CharField('Senha', max_length=1)
