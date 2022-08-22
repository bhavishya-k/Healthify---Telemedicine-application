from django.db import models
from django.db.models.fields import CharField, DateField
from user.models import user as USER
from doctor.choices import GENDER,STATES
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    Patient_id = models.BigAutoField(primary_key=True,unique=True)
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = PhoneNumberField()
    gender = CharField(max_length=1,choices=GENDER)
    dob = models.DateField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=6)
    state = models.CharField(max_length=50,choices=STATES)
    



