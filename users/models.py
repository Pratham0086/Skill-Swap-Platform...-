from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    AVAILABILITY_CHOICES = [
        ('weekends', 'Weekends'),
        ('weekdays', 'Weekdays'),
        ('evenings', 'Evenings'),
        ('custom', 'Custom'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    is_public = models.BooleanField(default=True)
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='weekends')
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
