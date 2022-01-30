from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
import datetime



class Master(models.Model):
    
    first_name = models.CharField(max_length=20, 
                                  help_text="Введіть ім'я",
                                  blank = True)
    
    last_name = models.CharField(max_length=20, 
                                 blank = False,
                                 help_text="Введіть фамілію")
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
class Device(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    type = models.CharField(help_text="Введіть тип пристрою",
                            max_length=128)
    
    def __str__(self):
        return f'{self.type}'
    
class Manufacture(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    manufacture = models.CharField(help_text="Введіть назву виробника продукту ",
                                   max_length=20)
    
    def __str__(self):
        return f'{self.manufacture}'      

class Form(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Унікальний UUID (створений автоматично)")

    def get_absolute_url(self):
        return reverse("form-detail", args=[str(self.id)])
    
    
    
    def __str__(self):
        return f'''Номер замовлення {self.id}
                   Клієнт: {self.last_name} {self.first_name}
                   Номер Телефону: {self.phone}
                   Пристрій: {self.type} - {self.manufacture} {self.model}
                   {self.open_orded}   -   {self.done_order}
                                            +0633381170
                '''
    
    
    first_name = models.CharField(max_length=20, 
                                  help_text="Введіть ім'я клієнта")
    
    last_name = models.CharField(max_length=20, 
                                 help_text="Введіть фамілію клієнта",
                                 blank=True) 
    
    phone = PhoneNumberField(null=False, blank=False, unique=True, help_text="Введіть номер телефону клієнта")
    
    type = models.ForeignKey(Device, on_delete=models.PROTECT, help_text="Тип девайсу")
    
    manufacture = models.ForeignKey(Manufacture, on_delete=models.PROTECT, help_text="Виробник")
    
    model = models.CharField(max_length=50, 
                             help_text="Введіть модель пристрою",
                             blank=True) 
    
    password = models.CharField(max_length=50, 
                                help_text="Введіть пароль доступу до пристрою",
                                blank=True,
                                default= 'Без паролю') 
    
    serial_number = models.CharField(max_length=50, 
                                     help_text="Введіть серійний номер пристрою",
                                     blank=True)
    
    reason = models.CharField(help_text="Виберіть тип пристрою",
                              max_length=128)
    
    is_repairable = models.CharField(help_text="Підлягає ремонту",
                                     choices=[('YES', 'Так'),
                                              ('NO', 'Ні') ],
                                     max_length=10,
                                     blank=True,
                                     default=False)
    
    price = models.DecimalField(max_digits=14, 
                                decimal_places=2,
                                help_text="Введіть ціну на замовлення",
                                null=False,
                                blank=False)
    
    took_the_orded = models.ForeignKey(Master, 
                                       on_delete=models.SET_DEFAULT, default='Admin',
                                       help_text="Приймав замовлення")
    
    open_orded = models.DateTimeField(help_text = 'Введіть дату відкриття замовлення', 
                                      default = datetime.datetime.now(),)
    
    done_order = models.DateTimeField(help_text = 'Введіть дату закриття замовлення',
                                      blank=True,
                                      null=True)
    
    is_notified = models.CharField(default=False,
                                   help_text= 'Чи був повідомлений клієнт',
                                   choices=[('YES', 'Так'),
                                            ('NO', 'Ні') ],
                                   max_length=10,
                                   blank=True)
    
    equipment = models.CharField(blank = True,
                                 max_length = 200,
                                 help_text= 'Комплектація до пристрою')
    
    
    

        
