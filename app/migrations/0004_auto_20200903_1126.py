# Generated by Django 2.0 on 2020-09-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_employee_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.BigIntegerField(default=1),
        ),
    ]
