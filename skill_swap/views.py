from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from skills.models import Skill
from swaps.models import SwapRequest

def home(request):
    """Home page showing other users' profiles for skill swapping"""
    if request.user.is_authenticated:
        # Get all public profiles except the current user's
        profiles = Profile.objects.filter(
            is_public=True
        ).exclude(
            user=request.user
        ).select_related('user').prefetch_related('user__userskill_set__skill')
        
        # Get current user's profile
        current_profile = Profile.objects.get_or_create(user=request.user)[0]
        
        context = {
            'profiles': profiles,
            'current_profile': current_profile,
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

@login_required
def request_swap(request, profile_id):
    """Handle skill swap requests"""
    if request.method == 'POST':
        target_profile = get_object_or_404(Profile, id=profile_id)
        
        # Check if request already exists
        existing_request = SwapRequest.objects.filter(
            sender=request.user,
            receiver=target_profile.user,
            status='pending'
        ).first()
        
        if existing_request:
            messages.warning(request, 'You have already sent a request to this user.')
        else:
            # Get or create a default skill for now
            default_skill, created = Skill.objects.get_or_create(name='General Skills')
            
            # Create new swap request
            SwapRequest.objects.create(
                sender=request.user,
                receiver=target_profile.user,
                skill_offered=default_skill,
                skill_requested=default_skill,
            )
            messages.success(request, f'Skill swap request sent to {target_profile.user.username}!')
        
        return redirect('home')
    
    return redirect('home') 