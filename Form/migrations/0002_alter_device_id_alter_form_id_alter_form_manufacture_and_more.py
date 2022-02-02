# Generated by Django 4.0 on 2022-02-02 19:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='form',
            name='manufacture',
            field=models.ForeignKey(help_text='Виробник', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Form.manufacture'),
        ),
        migrations.AlterField(
            model_name='form',
            name='open_orded',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 21, 53, 14, 443010), help_text='Введіть дату відкриття замовлення', null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='took_the_orded',
            field=models.ForeignKey(help_text='Приймав замовлення', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Form.master'),
        ),
        migrations.AlterField(
            model_name='form',
            name='type',
            field=models.ForeignKey(help_text='Тип девайсу', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Form.device'),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
