from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="avatars/", blank=True)
    about = models.TextField(blank=True)
    social_media = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.email} {self.username}"


class Address(models.Model):
    address_title = models.CharField(max_length=25)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="addresses"
    )
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"{self.address_title} {self.address_line_1}, {self.city}, {self.country}"
        )


class PhoneNumber(models.Model):
    phone_title = models.CharField(max_length=25)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="phone_numbers"
    )
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.phone_title} {self.number}"
