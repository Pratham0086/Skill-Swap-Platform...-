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
    return redirect('feedback_received')

@login_required
def leave_feedback(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id)
    if swap.status != 'accepted':
        messages.error(request, 'You can only leave feedback for accepted swaps.')
        return redirect('swaps_dashboard')
    if Feedback.objects.filter(swap=swap, from_user=request.user).exists():
        messages.warning(request, 'You have already left feedback for this swap.')
        return redirect('swaps_dashboard')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.swap = swap
            feedback.from_user = request.user
            feedback.to_user = swap.receiver if swap.sender == request.user else swap.sender
            feedback.save()
            messages.success(request, 'Feedback submitted!')
            return redirect('swaps_dashboard')
    else:
        form = FeedbackForm()
    return render(request, 'reviews/leave_feedback.html', {'form': form, 'swap': swap})

@login_required
def feedback_received(request):
    feedbacks = Feedback.objects.filter(to_user=request.user).order_by('-created_at')
    return render(request, 'reviews/feedback_received.html', {'feedbacks': feedbacks})

@login_required
def report_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, to_user=request.user)
    feedback.reported = True
    feedback.save()
    messages.info(request, 'Feedback reported for review.')
    return redirect('feedback_received')
