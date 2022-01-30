# Generated by Django 4.0 on 2022-01-28 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0003_remove_form_price_currency_alter_form_is_notified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='is_notified',
            field=models.CharField(blank=True, choices=[('YES', 'Так'), ('NO', 'Ні')], default=False, help_text='Чи був повідомлений клієнт', max_length=10),
        ),
        migrations.AlterField(
            model_name='form',
            name='open_orded',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 19, 59, 58, 18414), help_text='Введіть дату відкриття замовлення'),
        ),
    ]