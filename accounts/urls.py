from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LogInView, name='login'),
    path('logout/', LogOutView, name='logout'),
    path('activate/<uidb64>/<token>/', VerificationView, name='activate'),
    path('request-reset-email/', RequestResetEmail, name="request-reset-email"),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView, name='reset-password'),
]