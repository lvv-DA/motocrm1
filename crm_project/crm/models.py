# crm/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField 

# User Model
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensures no duplicate emails
    phone = PhoneNumberField(blank=True, null=True)  # Better phone number handling
    position = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', related_name='clients', on_delete=models.CASCADE)
    
    # Additional fields
    created_at = models.DateTimeField(auto_now_add=True)  # Tracks when the client was created
    updated_at = models.DateTimeField(auto_now=True)  # Tracks when the client was last updated
    
    # Optional: Add a status field
    status = models.CharField(
        max_length=20, 
        choices=[('active', 'Active'), ('inactive', 'Inactive')], 
        default='active'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Customer Model
class Customer(models.Model):
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    sales_rep = models.ForeignKey('SalesRepresentative', on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

class SalesRepresentative(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom User model
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Location Model
class Location(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    manager = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

# Opportunity Model
class Opportunity(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=100)
    expected_close_date = models.DateField()
    sales_rep = models.ForeignKey('SalesRepresentative', related_name='opportunities', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', related_name='opportunities', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.description

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
