from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SwapRequest
from .forms import SwapRequestForm
from django.contrib.auth.models import User
from skills.models import Skill
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def swaps_root_redirect(request):
    return redirect('swaps_dashboard')

@login_required
def send_swap_request(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    if receiver == request.user:
        messages.error(request, "You can't send a swap request to yourself.")
        return redirect('search_users_by_skill')
    if request.method == 'POST':
        form = SwapRequestForm(request.POST, user=request.user, receiver=receiver)
        if form.is_valid():
            skill_offered = form.cleaned_data['skill_offered']
            skill_requested = form.cleaned_data['skill_requested']
            # Prevent duplicate pending requests
            if SwapRequest.objects.filter(sender=request.user, receiver=receiver, skill_offered=skill_offered, skill_requested=skill_requested, status='pending').exists():
                messages.warning(request, 'You already have a pending request for this swap.')
            else:
                SwapRequest.objects.create(sender=request.user, receiver=receiver, skill_offered=skill_offered, skill_requested=skill_requested)
                messages.success(request, 'Swap request sent!')
            return redirect('swaps_dashboard')
    else:
        form = SwapRequestForm(user=request.user, receiver=receiver)
    return render(request, 'swaps/send_request.html', {'form': form, 'receiver': receiver})

@login_required
def swaps_dashboard(request):
    sent_swaps = SwapRequest.objects.filter(sender=request.user).order_by('-created_at')
    received_swaps = SwapRequest.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'swaps/dashboard.html', {'sent_swaps': sent_swaps, 'received_swaps': received_swaps})

@login_required
def accept_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, receiver=request.user)
    if swap.status == 'pending':
        swap.status = 'accepted'
        swap.save()
        messages.success(request, 'Swap request accepted!')
    return redirect('swaps_dashboard')

@login_required
def reject_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, receiver=request.user)
    if swap.status == 'pending':
        swap.status = 'rejected'
        swap.save()
        messages.info(request, 'Swap request rejected.')
    return redirect('swaps_dashboard')

@login_required
def cancel_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, sender=request.user)
    if swap.status == 'pending':
        swap.status = 'cancelled'
        swap.save()
        messages.info(request, 'Swap request cancelled.')
    return redirect('swaps_dashboard')

@login_required
def delete_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id, sender=request.user)
    if swap.status != 'accepted':
        swap.delete()
        messages.success(request, 'Swap request deleted.')
    else:
        messages.error(request, 'Accepted swaps cannot be deleted.')
    return redirect('swaps_dashboard')
