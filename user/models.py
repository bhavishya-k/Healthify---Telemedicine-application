from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_doctor(self, email, password=None, **extra_fields):
        
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields 
        ) 
        
        user.set_password(password)
        user.role = 'DOCTOR'
        user.save()
        return user

    def create_patient(self, email, password=None, **extra_fields):
        

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'PATIENT'        
        user.save()
        return user

    def create_hospital(self, email, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'HOSPITAL'
        user.save()
        return user

    def create_pharmacy(self, email,  password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'PHARMACY'
        user.save()
        return user

    def create_ambulance(self, email,  password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'AMBULANCE'
        user.save()
        return user

    def create_bloodbank(self, email,   password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'BLOODBANK'
        user.save()
        return user

    def create_lab(self, email, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.role = 'LAB'
        user.save()
        return user



    # def create_user(self, email, role, password=None, is_staff=False):
    #     if not email:
    #         raise ValueError(_("Users Must Have An Email Address"))
    #     if not password:
    #         raise ValueError(_("Password Not Provided"))
    #     if not role:
    #         raise ValueError(_("Role Not Provided"))
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         role=role,
    #     )
    #     user.is_staff = is_staff
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     user.save()

    #     return user

    def create_superuser(self, email, role, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not email:
            raise ValueError('Admin must have an email address')
        if not password:
            raise ValueError('Password Required')
        if not role:
            raise ValueError('Role Is Required')

        user = self.model(
            email=self.normalize_email(email),
             **extra_fields
        )
        user.set_password(password)
        user.role = user.ADMIN
        user.is_staff = True
        user.save()

        return user






class user(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'ADMIN'
    DOCTOR = 'DOCTOR'
    PATIENT = 'PATIENT'
    HOSPITAL = 'HOSPITAL'
    PHARMACY = 'PHARMACY'
    AMBULANCE = 'AMBULANCE'
    BLOODBANK = 'BLOODBANK'
    LAB = 'LAB'
    
    ROLE_CHIOCES = [
        (ADMIN, 'Admin'),
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
        (HOSPITAL, 'Hospital'),
        (PHARMACY, 'Pharmacy'),
        (AMBULANCE, 'Ambulance'),
        (BLOODBANK, 'BloodBank'),
        (LAB,'Lab'),

    ]
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(
        max_length=10, choices=ROLE_CHIOCES, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['role']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
       verbose_name = 'user'
       verbose_name_plural = 'users'

    # @property
    # def is_admin(self):
    #     return self.is_superuser

    # @property
    # def is_doctor(self):
    #     return (self.role == 'DOCTOR')

    # @property
    # def is_patient(self):
    #     return (self.role == 'PATIENT')

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.DOCTOR)


class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.PATIENT)


class HospitalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.HOSPITAL)


class PharmacyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.PHARMACY)


class AmbulanceManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.AMBULANCE)


class BloodbankManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.BLOODBANK)


class LabManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=user.LAB)


class Doctor(user):
    objects = DoctorManager()

    class Meta:
       proxy = True


class Patient(user):
    objects = PatientManager()

    class Meta:
       proxy = True


class Hospital(user):
    objects = HospitalManager()

    class Meta:
       proxy = True


class Pharmacy(user):
    objects = PharmacyManager()

    class Meta:
       proxy = True


class Ambulance(user):
    objects = AmbulanceManager()

    class Meta:
       proxy = True


class Bloodbank(user):
    objects = BloodbankManager()

    class Meta:
       proxy = True


class Lab(user):
    objects = LabManager()

    class Meta:
       proxy = True
