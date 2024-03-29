"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
    )
from django.contrib import admin

from leads import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('leads.urls', 'leads'), namespace="leads")),
    path('', include(('agents.urls', 'agents'), namespace="agents")),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logged_out/', LogoutView.as_view(), name = 'logged_out'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('reset-password/', PasswordResetView.as_view(), name = 'reset-password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)