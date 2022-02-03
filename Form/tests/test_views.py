from django.test import TestCase

from Form.models import Form
from django.urls import reverse

class FormListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 30 forms for pagination tests
        number_of_forms = 30
        for form_num in range(number_of_forms):
            Form.objects.create(first_name='Christian %s' % form_num,
                                last_name = 'Surname %s' % form_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/home/forms/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('forms'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('forms'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'Form/form_list.html')

    def test_pagination_is_25(self):
        resp = self.client.get(reverse('forms'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['form_list']) == 25)

    def test_lists_all_forms(self):
        resp = self.client.get(reverse('forms')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['form_list']) == 5)
