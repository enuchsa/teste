# urls.py
from django.urls import path

from heroes.auth.views import CreateUserAPIView

url_auth = [
    path('auth/register/', CreateUserAPIView.as_view(), name='auth_register'),
]
