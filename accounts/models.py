from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'users'
        