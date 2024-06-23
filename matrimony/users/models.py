from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass
    # GENDER_CHOICE = [
    #     ('M','Male'),
    #     ('F','Female'),
    #     ('o','Other'),
    # ]
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    # date_of_birth = models.DateField(null=True,blank=True)
    # phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.email