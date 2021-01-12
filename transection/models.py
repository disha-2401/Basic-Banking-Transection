from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.utils import timezone


class user(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('other', 'Other')
    )
    phone = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                           message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone], max_length=17, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male', null=True)
    email = models.EmailField()
    salary = models.IntegerField(max_length=12)
    balance = models.IntegerField(null=True)
    #
    # def __str__(self):
    #     return self.username

class transec(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=timezone.now)
    senderName = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    amount = models.IntegerField(max_length=30)
    #
    # def __str__(self):
    #     return self.senderName
