# Generated by Django 3.2 on 2021-04-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_alter_doctor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(help_text='Enter your mobile number of 10 digits', max_length=10),
        ),
    ]
