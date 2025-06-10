from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, fullname, email, password=None, **extra_fields):
        if not fullname:
            raise ValueError('The Fullname field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(fullname=fullname, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(fullname, email, password, **extra_fields)


class User(AbstractUser):
    username = None
    fullname = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'fullname'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.fullname
