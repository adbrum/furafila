'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
''''''
Created on 07/05/2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from datetime import datetime

from django.test import TestCase
from django.shortcuts import resolve_url as r
from furafila.core.models import Counter, Ticket, Service


class TicketModelTest(TestCase):
    def setUp(self):
        self.obj_ticket = Ticket(
            service_id=1,
            ticket='A001',
        )
        self.obj_ticket.save()

    def test_create(self):
        self.assertTrue(Ticket.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj_ticket.created_at, datetime)

    # def test_complete_use(self):
    #     self.assertIsInstance(self.obj_ticket.complete_use, datetime.hour)

    def test_str(self):
        self.assertEqual('A001', str(self.obj_ticket))

        # def test_get(self):
        #     """Get /senha/ must return code 200 """
        #     self.assertEqual(200, self.resp.status_code)
        #
        # def test_template(self):
        #     """Must use tickets/ticket_form.html"""
        #     self.assertTemplateUsed(self.resp, 'tickets/ticket_form.html')
        #
        # def test_new(self):
        #     service = self.obj_service.template
        #     ticket = self.obj_ticket.ticket
        #     self.assertEqual('A001', service + ticket)
