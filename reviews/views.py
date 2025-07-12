from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback
from .forms import FeedbackForm
from swaps.models import SwapRequest
from django.contrib.auth.models import User

# Create your views here.

@login_required
def reviews_root_redirect(request):
    return redirect('reviews:feedback_received')

@login_required
def leave_feedback(request, swap_id):
    # Only allow admins to leave feedback
    if not request.user.is_superuser:
        messages.error(request, 'Only administrators can leave feedback.')
        return redirect('swaps:dashboard')
    
    swap = get_object_or_404(SwapRequest, id=swap_id)
    if swap.status != 'accepted':
        messages.error(request, 'You can only leave feedback for accepted swaps.')
        return redirect('swaps:dashboard')
    if Feedback.objects.filter(swap=swap, from_user=request.user).exists():
        messages.warning(request, 'You have already left feedback for this swap.')
        return redirect('swaps:dashboard')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.swap = swap
            feedback.from_user = request.user
            feedback.to_user = swap.receiver if swap.sender == request.user else swap.sender
            feedback.save()
            messages.success(request, 'Feedback submitted!')
            return redirect('swaps:dashboard')
    else:
        form = FeedbackForm()
    return render(request, 'reviews/leave_feedback.html', {'form': form, 'swap': swap})

@login_required
def feedback_received(request):
    # Regular users can only see feedback they received
    if not request.user.is_superuser:
        feedbacks_received = Feedback.objects.filter(to_user=request.user).order_by('-created_at')
        context = {
            'feedbacks_received': feedbacks_received,
            'feedbacks_given': [],  # Empty for regular users
            'is_admin': False,
        }
    else:
        # Admins can see all feedback (received and given)
        feedbacks_received = Feedback.objects.filter(to_user=request.user).order_by('-created_at')
        feedbacks_given = Feedback.objects.filter(from_user=request.user).order_by('-created_at')
        context = {
            'feedbacks_received': feedbacks_received,
            'feedbacks_given': feedbacks_given,
            'is_admin': True,
        }
    
    return render(request, 'reviews/feedback_received.html', context)

@login_required
def report_feedback(request, feedback_id):
    # Only allow users to report feedback they received
    feedback = get_object_or_404(Feedback, id=feedback_id, to_user=request.user)
    feedback.reported = True
    feedback.save()
    messages.info(request, 'Feedback reported for review.')
    return redirect('reviews:feedback_received')
