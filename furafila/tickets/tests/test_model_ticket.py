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

from furafila.core.models import Ticket


class TicketModelTest(TestCase):
    def setUp(self):
        self.obj_ticket = Ticket(
            service_id=1,
            ticket='A1',
            complete_use=datetime.now()
        )
        self.obj_ticket.save()

    def test_create(self):
        self.assertTrue(Ticket.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj_ticket.created_at, datetime)

    def test_complete_use(self):
        self.assertIsInstance(self.obj_ticket.complete_use, datetime)

    def test_str(self):
        self.assertEqual('A1', str(self.obj_ticket))
