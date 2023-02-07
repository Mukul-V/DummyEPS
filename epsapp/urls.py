from django.urls import path
from epsapp.views.AdminLoginAPI import AdminLoginAPI

urlpatterns = [
    path('admin-login/', AdminLoginAPI.as_view(), name='login_view'),
]
