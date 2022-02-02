from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Device, Manufacture, Master, Form


class EditForm(forms.Form):
    
    first_name = forms.CharField(max_length=20,
                                 label="Ім'я клієнта")
    
    last_name = forms.CharField(max_length=20, 
                                label='Фамілія клієнта') 
    
    phone = forms.CharField(max_length=13,
                            min_length=13,
                            label="Контакт клієнта")
    
    type = forms.ModelChoiceField(queryset=Device.objects.all(),
                                  label='Тип пристрою',
                                  initial='')
    
    manufacture = forms.ModelChoiceField(queryset=Manufacture.objects.all(),
                                         label='Виробник',
                                         initial='')
    
    model = forms.CharField(max_length=20, 
                            label="Модель пристрою",) 
    
    password = forms.CharField(max_length=30, 
                               label="Пароль доступу до пристрою",
                               initial='без паролю') 
    
    serial_number = forms.CharField(max_length=30, 
                                    label="Серійний номер продукта",)
    
    reason = forms.CharField(label="Причина поломки",
                             max_length=128)

    
    price = forms.DecimalField(max_digits=7, 
                               decimal_places=2,
                               label='Ціна замовлення')
    
    took_the_order = forms.ModelChoiceField(queryset=Master.objects.all(),
                                            label = 'Приймав замовлення',
                                            initial= '')
    
    # open_orded = forms.DateTimeField(label = 'Відкриття замовлення', 
    #                                  initial = datetime.datetime.now(),
    #                                  input_formats = ['%Y-%m-%d %H:%M'])
    
    done_order = forms.DateTimeField(label = 'Закриття замовлення',
                                     input_formats=['%Y-%m-%d %H:%M'])
            
    is_repairable = forms.ChoiceField(choices=[('YES', 'Так'),
                                               ('NO', 'Ні') ], 
                                      required=True,
                                      label='Ремонтоспроможність',
                                      initial='')
    
    is_notified = forms.ChoiceField(label= 'Повідомлений клієнт',
                                     choices=[('YES', 'Так'),
                                               ('NO', 'Ні') ], 
                                     required=True,
                                     initial='',)
    
    equipment = forms.CharField(max_length =200,
                                label = 'Комплектація до пристрою')

    
    def clean_last_name(self):
        
        last_name = self.cleaned_data['last_name']
                
        if not last_name.isalpha():
            raise forms.ValidationError(_("Ім'я має містити лише літери без пробілу"))
        
        return last_name
    
    
    def clean_first_name(self):
    
        first_name = self.cleaned_data['first_name']
        
        if not first_name.isalpha():
            raise forms.ValidationError(_('Фамілія має містити лише літери без пробілу'))
        
        return first_name
    
    
    def clean_phone(self):
        
        phone = self.cleaned_data['phone']
        
        if phone[0] != '+' or not phone[1:].isdigit():
            raise forms.ValidationError(_('Номер телефону повинен містити "+380" та 9 цифр'))          
        
        return phone
