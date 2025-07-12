from django.urls import path
from . import views

urlpatterns = [
    path('', views.swaps_root_redirect),
    path('send/<int:receiver_id>/', views.send_swap_request, name='send_swap_request'),
    path('dashboard/', views.swaps_dashboard, name='swaps_dashboard'),
    path('accept/<int:swap_id>/', views.accept_swap, name='accept_swap'),
    path('reject/<int:swap_id>/', views.reject_swap, name='reject_swap'),
    path('cancel/<int:swap_id>/', views.cancel_swap, name='cancel_swap'),
    path('delete/<int:swap_id>/', views.delete_swap, name='delete_swap'),
] 