from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, UserSkill
from .forms import UserSkillForm
from users.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def skill_dashboard(request):
    offered_skills = UserSkill.objects.filter(user=request.user, skill_type='offered')
    wanted_skills = UserSkill.objects.filter(user=request.user, skill_type='wanted')
    skills_exist = Skill.objects.exists()
    if request.method == 'POST' and skills_exist:
        if 'add_offered' in request.POST:
            skill_name = request.POST.get('offered_skill_name', '').strip()
            if skill_name:
                skill, _ = Skill.objects.get_or_create(name__iexact=skill_name, defaults={'name': skill_name})
                if UserSkill.objects.filter(user=request.user, skill=skill, skill_type='offered').exists():
                    messages.warning(request, f'You already have this skill as offered.')
                else:
                    UserSkill.objects.create(user=request.user, skill=skill, skill_type='offered')
                    messages.success(request, f'Skill "{skill}" added as offered.')
            return redirect('skills:dashboard')
        elif 'add_wanted' in request.POST:
            skill_name = request.POST.get('wanted_skill_name', '').strip()
            if skill_name:
                skill, _ = Skill.objects.get_or_create(name__iexact=skill_name, defaults={'name': skill_name})
                if UserSkill.objects.filter(user=request.user, skill=skill, skill_type='wanted').exists():
                    messages.warning(request, f'You already have this skill as wanted.')
                else:
                    UserSkill.objects.create(user=request.user, skill=skill, skill_type='wanted')
                    messages.success(request, f'Skill "{skill}" added as wanted.')
            return redirect('skills:dashboard')
    context = {
        'offered_skills': offered_skills,
        'wanted_skills': wanted_skills,
        'skills_exist': skills_exist,
    }
    return render(request, 'skills/dashboard.html', context)

@login_required
def delete_user_skill(request, skill_id):
    userskill = UserSkill.objects.get(id=skill_id, user=request.user)
    userskill.delete()
    messages.success(request, 'Skill removed.')
    return redirect('skills:dashboard')

@login_required
def search_users_by_skill(request):
    query = request.GET.get('q', '')
    availability = request.GET.get('availability', '')
    location = request.GET.get('location', '')
    users = User.objects.filter(profile__is_public=True)
    if query:
        users = users.filter(userskill__skill__name__icontains=query, userskill__skill_type='offered')
    if availability:
        users = users.filter(profile__availability=availability)
    if location:
        users = users.filter(profile__location__icontains=location)
    users = users.distinct()
    skills = Skill.objects.all().order_by('name')
    context = {
        'users': users,
        'skills': skills,
        'query': query,
        'availability': availability,
        'location': location,
    }
    return render(request, 'skills/search.html', context)
