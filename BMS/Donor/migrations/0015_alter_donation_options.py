# Generated by Django 3.2 on 2021-04-29 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0014_alter_donation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ['-date']},
        ),
    ]
