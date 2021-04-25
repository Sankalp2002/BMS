# Generated by Django 3.2 on 2021-04-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0011_alter_donor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(help_text='Enter your address', max_length=128),
        ),
        migrations.AlterField(
            model_name='donor',
            name='age',
            field=models.PositiveIntegerField(default=18, help_text='Enter your age'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(help_text='Enter your name', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=models.PositiveIntegerField(help_text='Enter your mobile number of 10 digits'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]
