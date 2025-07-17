from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from datetime import date
from django.core.validators import RegexValidator
# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, username, **extrafields):
        if not email:
            raise ValueError(" Email is invalid! ")
        email = self.normalize_email(email)
        User = self.model(email = email, username = username, **extrafields)
        User.set_password(password)
        User.save()
        return User
    
    def create_user(self, email, password = None, username = None, **extrafields):
        extrafields.setdefault("is_staff" , False)
        extrafields.setdefault("is_superuser", False)
        return self._create_user(email, password, username, **extrafields)

    def create_superuser(self, email, password = None, username = None, **extrafields):
        extrafields.setdefault("is_staff" , True)
        extrafields.setdefault("is_superuser", True)
        return self._create_user(email, password, username, **extrafields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=28, primary_key=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at= models.DateField(default= date.today)
    last_login =models.DateField(default=date.today)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.username