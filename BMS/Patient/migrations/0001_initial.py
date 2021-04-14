# Generated by Django 3.2 on 2021-04-14 13:52

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('email', models.EmailField(max_length=32)),
                ('age', models.PositiveIntegerField(default=18)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('bloodType', models.CharField(max_length=3)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctor')),
            ],
        ),
    ]
