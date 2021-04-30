# Generated by Django 3.2 on 2021-04-30 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BRtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodType', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], help_text='Enter the Blood Group required', max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='bloodType',
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='btype',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blood.brtype'),
        ),
    ]