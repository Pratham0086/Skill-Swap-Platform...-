from django import forms
from .models import SwapRequest
from skills.models import Skill, UserSkill

class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['skill_offered', 'skill_requested']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        receiver = kwargs.pop('receiver', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['skill_offered'].queryset = Skill.objects.filter(userskill__user=user, userskill__skill_type='offered')
        if receiver:
            self.fields['skill_requested'].queryset = Skill.objects.filter(userskill__user=receiver, userskill__skill_type='offered') 