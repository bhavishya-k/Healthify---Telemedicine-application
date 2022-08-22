from django.db import models
from django.db.models.base import Model
from user.models import user as USER
from doctor.choices import STATES
from phonenumber_field.modelfields import PhoneNumberField


FLAG = [
    ('H','HOSPITAL'),
    ('C','CLINIC'),
]

TYPE = [
    ('G','GOVERNMENT'),
    ('P','PRIVATE'),
]
class Hospital(models.Model):
    Hospital_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    user = models.ForeignKey(USER,on_delete=models.CASCADE,related_name='HospitalUser')
    name = models.CharField(max_length=255)
    flag = models.CharField(max_length=10,choices=FLAG)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    town = models.CharField(max_length=30,null=True)
    village = models.CharField(max_length=30,null=True)
    district = models.CharField(max_length=30)
    subdistrict = models.CharField(max_length=30,null=True)
    postalcode = models.CharField(max_length=6)
    state = models.CharField(max_length=100,choices=STATES)
    type = models.CharField(max_length=10,choices=TYPE)
    website = models.URLField(max_length=100,null=True)
    registeration_number = models.CharField(max_length=30)
    establishdate = models.DateField()
    lat = models.DecimalField(max_digits=10,decimal_places=8,null=True)
    lng = models.DecimalField(max_digits=11,decimal_places=8,null=True)
    accreditation = models.CharField(max_length=255,null=True)
    num_of_doctors = models.IntegerField(null=True)
    num_of_medicalconsultants = models.IntegerField(null=True)
    num_of_beds = models.IntegerField(null=True)
    num_of_privatewards = models.IntegerField(null=True)
    num_of_bedsews = models.IntegerField(null=True)
    contact = PhoneNumberField()
    status = models.BooleanField(default=True)
    adminapproval = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class HealthcareType(models.Model):
    Healthcare_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    name = models.CharField(max_length=30)

class Speciality(models.Model):
    Speciality_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    name = models.CharField(max_length=30)

class Facilities(models.Model):
    Facilities_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    name = models.CharField(max_length=30)

class AyushType(models.Model):
    Ayush_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    name = models.CharField(max_length=30)

class MiscellaneousFacilities(models.Model):
    MFacilities_id = models.BigAutoField(primary_key=True,unique=True,blank=False,null=False)
    name = models.CharField(max_length=30)

class HospitalAyushtype(models.Model):
    Hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='HospitalAyush')
    Ayush_id = models.ForeignKey(AyushType,on_delete=models.CASCADE,related_name='AyushHospital')

class HospitalFacilities(models.Model):
    Hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    Facilities_id = models.ForeignKey(Facilities,on_delete=models.CASCADE)

class HospitalSpecialities(models.Model):
    Hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    Speciality_id = models.ForeignKey(Speciality,on_delete=models.CASCADE)

class HospitalHealthcare(models.Model):
    Hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    Healthcare_id = models.ForeignKey(HealthcareType,on_delete=models.CASCADE)

class HospitalMFacilies(models.Model):
    Hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    MFacilities_id = models.ForeignKey(MiscellaneousFacilities,on_delete=models.CASCADE)













        











