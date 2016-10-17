'''
Created on 07/05/2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''

from django.test import TestCase

from furafila.core.models import Ticket, Service
from django.shortcuts import resolve_url as r


class NewTicketTest(TestCase):
    def setUp(self):

        ticket = self.obj_ticket = Ticket(
            service_id=1,
            ticket='0',
        )
        self.obj_ticket.save()

        service_ = self.obj_service = Service(
            name='Atendimento Geral',
            description = '',
            prefixo = 'A',
            quantity_of_tickets = 200,
            state = True,
        )
        self.obj_service.save()

        service = Service.objects.get(name='Atendimento Geral')

        pos = Ticket.objects.filter(service_id=service.pk).last()

        # for i in pos:
        print('XXXXX ', pos.ticket )

        self.counter(service.prefixo, pos.ticket)

    def counter(self, service, pos):
        pos = int(pos)
        pos += 1
        self.pos = (service + str(pos))
        print(service + str(pos))

    def test_create(self):
        self.assertTrue(Ticket.objects.exists())

    # def test_new_ticket(self):
    #     self.assertEqual('A1', self.pos)

