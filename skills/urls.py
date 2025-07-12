from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.skill_dashboard, name='dashboard'),
    path('delete/<int:skill_id>/', views.delete_user_skill, name='delete_user_skill'),
    path('search/', views.search_users_by_skill, name='search_users_by_skill'),
] 