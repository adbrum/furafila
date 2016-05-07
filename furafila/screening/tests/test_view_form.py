from django.test import TestCase


class PointAccessNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/triagem/')

    def test_get(self):
        """Get /screening/ must return code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'screening/screening_form.html')

