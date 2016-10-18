from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Ticket(models.Model):  # Senha
    service = models.ForeignKey('Service', verbose_name='serviço')
    ticket = models.CharField('senha', max_length=4)
    created_at = models.DateTimeField('emitida em', auto_now_add=True)
    complete_use = models.DateTimeField('concluída', blank=True)

    class Meta:
        verbose_name_plural = 'senha'
        verbose_name = 'senhas'

    def __str__(self):
        return self.ticket


class Service(models.Model):  # Serviços
    name = models.CharField('nome', max_length=100)
    description = models.TextField('descrição', max_length=255)
    prefixo = models.CharField('prefixo', max_length=1)
    quantity_of_tickets = models.IntegerField('quanditade')
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'serviços'
        verbose_name = 'serviço'
        ordering = ('name',)

    def __str__(self):
        return self.name


# class Counter(models.Model):  # Contador
#     ticket = models.ForeignKey('Ticket', verbose_name='senha')
#     prefixo = models.ForeignKey('Service',  verbose_name='prefixo')
#     total = models.IntegerField('Total', validators=[MaxValueValidator(999)])
#
#     class Meta:
#         verbose_name_plural = 'contadores'
#         verbose_name = 'contador'
#
#     def __str__(self):
#         return self.set

# class Attendance(models.Model):  # Atendimento
#     user = models.OneToOneField(User)
#     service = models.ForeignKey('Service')
#     priority = models.ForeignKey('Priority')
#     accesspoint = models.ForeignKey('AccessPoint')
#     ticket = models.CharField('Senha', max_length=4)
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     check_in = models.DateTimeField('Entrada', auto_now=True)
#     check_out = models.DateTimeField('Saida', null=True)
#
#
# class Position(models.Model):  # Cargos
#     name = models.CharField('Nome', max_length=100)
#     description = models.TextField('Descrição', max_length=255)
#
#     class Meta:
#         verbose_name_plural = 'Cargos'
#         verbose_name = 'Cargo'
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name
#
#
# class AccessPoint(models.Model):  # Ponto de Acesso
#     name = models.CharField('Nome', max_length=100)
#     quantity = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = 'Pontos de acesso'
#         verbose_name = 'Ponto de acesso'
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name
#
#
# class Priority(models.Model):  # Prioridade
#     name = models.CharField('Nome', max_length=100)
#     description = models.TextField('Descrição', max_length=255)
#     priority = models.IntegerField()
#     state = models.BooleanField()
#
#     class Meta:
#         verbose_name_plural = 'Prioridades'
#         verbose_name = 'Prioridade'
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name



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
