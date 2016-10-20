from django.test import TestCase
from django.shortcuts import resolve_url as r


class PointAccessNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('ticket:new'))

    def test_get(self):
        """Get /screening/ must return code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use ticket_form.html"""
        self.assertTemplateUsed(self.resp, 'tickets/ticket_form.html')

