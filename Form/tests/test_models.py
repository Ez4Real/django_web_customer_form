from django.test import TestCase
from Form.models import Form

class FormModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Form.objects.create(first_name='Big',
                            last_name='Bob')

    def test_last_name_label(self):
        form=Form.objects.get(id=1)
        field_label = form._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')
        
    def test_first_name_label(self):
        form=Form.objects.get(id=1)
        field_label = form._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')    
        
    def test_date_of_open_order(self):
        form=Form.objects.get(id=1)
        field_label = form._meta.get_field('open_order').verbose_name
        self.assertEquals(field_label,'open order')

    def test_date_of_done_order(self):
        form=Form.objects.get(id=1)
        field_label = form._meta.get_field('done_order').verbose_name
        self.assertEquals(field_label,'done order')
    
    def test_last_name_max_length(self):
        form=Form.objects.get(id=1)
        max_length = form._meta.get_field('last_name').max_length
        self.assertEquals(max_length,20)
        
    def test_first_name_max_length(self):
        form=Form.objects.get(id=1)
        max_length = form._meta.get_field('first_name').max_length
        self.assertEquals(max_length,20)

    def test_password_max_length(self):
        form=Form.objects.get(id=1)
        max_length = form._meta.get_field('password').max_length
        self.assertEquals(max_length,50)
        
    def test_reason_max_length(self):
        form=Form.objects.get(id=1)
        max_length = form._meta.get_field('reason').max_length
        self.assertEquals(max_length,128)
        
    def test_serial_number_max_length(self):
        form=Form.objects.get(id=1)
        max_length = form._meta.get_field('serial_number').max_length
        self.assertEquals(max_length,50)
        
    def test_price_max_digits_and_decimal_places(self):
        form=Form.objects.get(id=1)
        max_digits = form._meta.get_field('price').max_digits
        decimal_places = form._meta.get_field('price').decimal_places
        self.assertEquals(max_digits,14)
        self.assertEquals(decimal_places,2)

    def test_object_name_is_type_manufacture_model(self):
        form=Form.objects.get(id=1)
        expected_object_name = '%s %s %s' % (form.type, form.manufacture, form.model)
        self.assertEquals(expected_object_name,str(form))

    def test_get_absolute_url(self):
        form=Form.objects.get(id=1)
        self.assertEquals(form.get_absolute_url(),'/home/form/1/details')
        
