from django.db import models
from user.models import user as USER
from phonenumber_field.modelfields import PhoneNumberField
from .choices import GENDER,STATES



class Doctor(models.Model):

    
    doctor_id = models.BigAutoField(unique=True,primary_key=True)
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50 , null=True)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER)
    dob = models.DateField()
    currentaddress_street = models.CharField(max_length=255)
    currentaddress_city = models.CharField(max_length=20)
    currentaddress_district = models.CharField(max_length=20)
    currentaddress_state = models.CharField(max_length=50,choices=STATES)
    currentaddress_postalcode = models.CharField(max_length=6)
    permaddress_street = models.CharField(max_length=255)
    permaddress_city = models.CharField(max_length=20)
    permaddress_district = models.CharField(max_length=20)
    permaddress_state = models.CharField(max_length=50,choices=STATES)
    permaddress_postalcode = models.CharField(max_length=6)
    fathersname = models.CharField(max_length=50)
    contact = PhoneNumberField()
    experience = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return (self.firstname + self.lastname)



