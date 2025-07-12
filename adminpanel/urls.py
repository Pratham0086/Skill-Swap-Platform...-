from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='adminpanel_login'),
    path('', views.dashboard, name='adminpanel_dashboard'),
    path('ban_user/<int:user_id>/', views.ban_user, name='ban_user'),
    path('unban_user/<int:user_id>/', views.unban_user, name='unban_user'),
    path('send_message/', views.send_message, name='send_message'),
    path('download_users_csv/', views.download_users_csv, name='download_users_csv'),
    path('download_swaps_csv/', views.download_swaps_csv, name='download_swaps_csv'),
    path('download_feedback_csv/', views.download_feedback_csv, name='download_feedback_csv'),
] 