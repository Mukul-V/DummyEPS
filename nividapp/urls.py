from django.urls import path
from .src.views.BaseView import BaseView

urlpatterns = [
    path('base-url/', BaseView.as_view(), name="Base_View"),
]

