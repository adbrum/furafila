from django.test import TestCase


class PointAccessNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Get /home/ must return code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

