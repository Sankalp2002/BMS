# Patient
from django.db import models
from Doctor import models as dmodels

# Create your models here.

class Patient(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    patientId = models.CharField(primary_key=True,max_length=128,help_text="Patient ID is for unique identification.")
    doctorId = models.CharField(max_length=128,blank=True)
    name = models.CharField(max_length=32, help_text="Enter your name",blank=False)
    age = models.PositiveIntegerField(default=18, help_text="Enter your age",blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M',blank=False)
    address = models.CharField(max_length=128, help_text="Enter your address",blank=False)
    phone = models.CharField(max_length=10,help_text="Enter your mobile number of 10 digits",blank=False)
    email = models.EmailField(max_length=32,blank=False)
    bloodType = models.CharField(max_length=3,choices=BLOOD_GROUP_CHOICES,blank=False)

    def __str__(self):
        return self.patientId
        # return str(self.patientId)+str(self.bloodType)
