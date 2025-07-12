from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

# Create your models here.

class SwapRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_swaps')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_swaps')
    skill_offered = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_swaps')
    skill_requested = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='requested_swaps')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} offers {self.skill_offered} for {self.skill_requested} from {self.receiver} ({self.status})"
