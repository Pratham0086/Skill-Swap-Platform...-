"""
URL configuration for skill_swap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from skill_swap import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('request-swap/<int:profile_id>/', core_views.request_swap, name='request_swap'),
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.urls', namespace='adminpanel')),
    path('users/', include('users.urls')),
    path('skills/', include('skills.urls', namespace='skills')),
    path('swaps/', include('swaps.urls', namespace='swaps')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
