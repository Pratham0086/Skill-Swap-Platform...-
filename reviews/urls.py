from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_root_redirect),
    path('leave/<int:swap_id>/', views.leave_feedback, name='leave_feedback'),
    path('received/', views.feedback_received, name='feedback_received'),
    path('report/<int:feedback_id>/', views.report_feedback, name='report_feedback'),
] 