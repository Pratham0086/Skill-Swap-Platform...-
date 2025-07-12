from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from users.models import Profile
from skills.models import Skill, UserSkill
from swaps.models import SwapRequest
from reviews.models import Feedback
from django.contrib.auth.models import User
from skills.forms import SkillForm
from django.http import HttpResponse
import csv

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('adminpanel_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminpanel_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin user.')
    return render(request, 'adminpanel/login.html')

@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    users = User.objects.all()
    skills = Skill.objects.all()
    swaps = SwapRequest.objects.all()
    feedbacks = Feedback.objects.all()
    skill_form = SkillForm()
    if request.method == 'POST' and 'add_skill' in request.POST:
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save()
            messages.success(request, 'Skill added!')
            return redirect('adminpanel_dashboard')
    return render(request, 'adminpanel/dashboard.html', {
        'users': users,
        'skills': skills,
        'swaps': swaps,
        'feedbacks': feedbacks,
        'skill_form': skill_form,
    })

@user_passes_test(lambda u: u.is_staff)
def ban_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f'User {user.username} has been banned.')
    return redirect('adminpanel_dashboard')

@user_passes_test(lambda u: u.is_staff)
def unban_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f'User {user.username} has been unbanned.')
    return redirect('adminpanel_dashboard')

@user_passes_test(lambda u: u.is_staff)
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('platform_message')
        # For demo: store in session or show as a flash message
        request.session['platform_message'] = message
        messages.success(request, 'Platform-wide message sent!')
    return redirect('adminpanel_dashboard')

@user_passes_test(lambda u: u.is_staff)
def download_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Username', 'Email', 'Is Active', 'Is Staff'])
    for user in User.objects.all():
        writer.writerow([user.id, user.username, user.email, user.is_active, user.is_staff])
    return response

@user_passes_test(lambda u: u.is_staff)
def download_swaps_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="swaps.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Sender', 'Receiver', 'Offered', 'Requested', 'Status', 'Created', 'Updated'])
    for swap in SwapRequest.objects.all():
        writer.writerow([swap.id, swap.sender.username, swap.receiver.username, swap.skill_offered.name, swap.skill_requested.name, swap.status, swap.created_at, swap.updated_at])
    return response

@user_passes_test(lambda u: u.is_staff)
def download_feedback_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'From', 'To', 'Rating', 'Comment', 'Reported', 'Created'])
    for fb in Feedback.objects.all():
        writer.writerow([fb.id, fb.from_user.username, fb.to_user.username, fb.rating, fb.comment, fb.reported, fb.created_at])
    return response
