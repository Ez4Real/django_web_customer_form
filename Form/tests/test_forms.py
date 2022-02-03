from django.test import TestCase
import datetime
from django.utils import timezone
from Form.forms import EditForm

class EditFormTest(TestCase):
    
    def test_edit_form_open_order_label(self):
        form = EditForm()
        self.assertTrue(form.fields['open_order'].label == None or form.fields['open_order'].label == 'Відкриття замовлення')   
        
    def test_edit_form_open_order_disabled(self):
        form = EditForm()
        self.assertTrue(form.fields['open_order'].disabled == True)

    def test_edit_form_done_order_label(self):
        form = EditForm()
        self.assertTrue(form.fields['done_order'].label == None or form.fields['done_order'].label == 'Закриття замовлення')
        
    def test_edit_form_first_name_label(self):
        form = EditForm()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == "Ім'я клієнта")
        
    def test_edit_form_first_name_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['first_name'].max_length == 20)
        
    def test_edit_form_last_name_label(self):
        form = EditForm()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Фамілія клієнта')
        
    def test_edit_form_last_name_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['last_name'].max_length == 20)        
    
    def test_edit_form_phone_label(self):
        form = EditForm()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Контакт клієнта')
        
    def test_edit_form_last_name_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['phone'].max_length == 13) 
        
    def test_edit_form_last_name_min_length(self):
        form=EditForm()
        self.assertTrue(form.fields['phone'].min_length == 13) 
        
    def test_edit_form_type_label(self):
        form = EditForm()
        self.assertTrue(form.fields['type'].label == None or form.fields['type'].label == 'Тип пристрою')
        
    def test_edit_form_manufacture_label(self):
        form = EditForm()
        self.assertTrue(form.fields['manufacture'].label == None or form.fields['manufacture'].label == 'Виробник')
        
    def test_edit_form_model_label(self):
        form = EditForm()
        self.assertTrue(form.fields['model'].label == None or form.fields['model'].label == 'Модель пристрою')
        
    def test_edit_form_model_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['model'].max_length == 20)  
        
        
    def test_edit_form_password_label(self):
        form = EditForm()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль доступу до пристрою')
        
    def test_edit_form_password_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['password'].max_length == 30)  
        
    def test_edit_form_model_initial(self):
        form=EditForm()
        self.assertTrue(form.fields['password'].initial == 'без паролю') 
        
    def test_edit_form_serial_number_label(self):
        form = EditForm()
        self.assertTrue(form.fields['serial_number'].label == None or form.fields['serial_number'].label == 'Серійний номер продукта')
        
    def test_edit_form_serial_number_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['serial_number'].max_length == 30)   
        
    def test_edit_form_reason_label(self):
        form = EditForm()
        self.assertTrue(form.fields['reason'].label == None or form.fields['reason'].label == 'Причина поломки')
        
    def test_edit_form_reason_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['reason'].max_length == 128)  
        
    def test_edit_form_phone_label(self):
        form = EditForm()
        self.assertTrue(form.fields['price'].label == None or form.fields['price'].label == 'Ціна замовлення')
        
    def test_edit_form_price_max_digits(self):
        form=EditForm()
        self.assertTrue(form.fields['price'].max_digits == 7) 
        
    def test_edit_form_price_decimal_places(self):
        form=EditForm()
        self.assertTrue(form.fields['price'].decimal_places == 2) 
        
    def test_edit_form_took_the_order_label(self):
        form = EditForm()
        self.assertTrue(form.fields['took_the_order'].label == None or form.fields['took_the_order'].label == 'Приймав замовлення')
        
    def test_edit_form_is_repairable_label(self):
        form = EditForm()
        self.assertTrue(form.fields['is_repairable'].label == None or form.fields['is_repairable'].label == 'Ремонтоспроможність')
        
    def test_edit_form_is_repairable_choices(self):
        form = EditForm()
        self.assertTrue(form.fields['is_repairable'].choices == [('YES', 'Так'),
                                                                 ('NO', 'Ні')])
        
    def test_edit_form_is_repairable_required(self):
        form = EditForm()
        self.assertTrue(form.fields['is_repairable'].required == True)
        
    def test_edit_form_is_notified_label(self):
        form = EditForm()
        self.assertTrue(form.fields['is_notified'].label == None or form.fields['is_notified'].label == 'Повідомлений клієнт')
        
    def test_edit_form_is_notified_choices(self):
        form = EditForm()
        self.assertTrue(form.fields['is_notified'].choices == [('YES', 'Так'),
                                                                 ('NO', 'Ні')])
        
    def test_edit_form_is_notified_required(self):
        form = EditForm()
        self.assertTrue(form.fields['is_notified'].required == True)
        
    def test_edit_form_equipment_label(self):
        form = EditForm()
        self.assertTrue(form.fields['equipment'].label == None or form.fields['equipment'].label == 'Комплектація до пристрою')
        
    def test_edit_form_equipment_max_length(self):
        form=EditForm()
        self.assertTrue(form.fields['equipment'].max_length == 200)
    
    


        
    
        
        
