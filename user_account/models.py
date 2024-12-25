from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django_countries.fields import CountryField
from django.utils.timezone import now
from datetime import timedelta
import uuid
from .validators import validate_password,validate_phone_number
from datetime import date

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password,**extrafields):
        if not email:
            raise ValueError("The Email Field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None,**extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        return self.create_user(username,email,password,**extrafields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    password = models.CharField(max_length=18,validators=[validate_password])
    phone_number = models.CharField(max_length=15,validators=[validate_phone_number])
    country = CountryField()
    city = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    email_token = models.UUIDField(default=uuid.uuid4)
    cookie_token = models.UUIDField(default=uuid.uuid4)
    is_emailVerified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number']

    def __str__(self):
        return self.username
    
class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def Check_Links(email,token,cool_off=10):
        time_threshold  = now() - timedelta(minutes=cool_off)
        link = PasswordReset.objects.filter(email=email,token=token,timestamp__gte=time_threshold).first()
        return link if link else None

class LoginAttempt(models.Model):
    username = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def check_attempts(ip_address,limit=5,cool_off=5):
        time_threshold = now() - timedelta(minutes=cool_off)
        attempts = LoginAttempt.objects.filter(ip_address=ip_address,timestamp__gte=time_threshold).count()
        return attempts>=limit
