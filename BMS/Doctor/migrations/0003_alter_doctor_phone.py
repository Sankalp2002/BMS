# Generated by Django 3.2 on 2021-04-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_alter_doctor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.PositiveIntegerField(help_text='Enter your mobile number', max_length=10),
        ),
    ]
