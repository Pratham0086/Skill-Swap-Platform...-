from django import forms
from .models import Skill, UserSkill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 2 or name.lower() in ['help', 'test', 'skill']:
            raise forms.ValidationError('Please enter a more specific skill name.')
        return name

class UserSkillForm(forms.Form):
    skill_name = forms.CharField(label='Skill Name', max_length=50)
    skill_type = forms.ChoiceField(choices=UserSkill.SKILL_TYPE_CHOICES) 