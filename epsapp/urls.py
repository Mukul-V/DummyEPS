from django.urls import path
from epsapp.views.AdminLoginAPI import AdminLoginAPI
from epsapp.views.AdminLogout import AdminLogout
from epsapp.views.BaseView import BaseView

urlpatterns = [
    path('base-view/', BaseView.as_view(), name='base_view'),
    path('admin-login/', AdminLoginAPI.as_view(), name='login_view'),
    path('admin-logout/', AdminLogout.as_view(), name='logout_view'),
]
