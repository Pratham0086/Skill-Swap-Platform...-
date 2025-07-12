from django.db import models
from django.contrib.auth.models import User
from swaps.models import SwapRequest

# Create your models here.

class Feedback(models.Model):
    swap = models.ForeignKey(SwapRequest, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_given')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    reported = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} ({self.rating})"
