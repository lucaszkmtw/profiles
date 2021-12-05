from abc import abstractstaticmethod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models her
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        """crear nuevo user profile"""
        if not email:
            raise ValueError('usuario debe tener un email')

        email = self.normalize_email(email)
        user= self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self.db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)    
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


    def get_full_name(self):
        return self.name
        
    def get_short_name(self):
        return self.name