from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.contrib import admin


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        password = make_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

    

class User(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email


# class Address(models.Model):
#     wilaya = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     strete = models.CharField(max_length=255)


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    # address = models.ForeignKey(Address, on_delete=models.PROTECT)

  

    class Meta:
     
        permissions = [
            ('view_history', 'Can view history')
        ]

   