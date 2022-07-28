from MyUser import views
from django.urls import path

urlpatterns = [
    path('is_staff', views.GetStaffStatusView.as_view(), name='is_staff'),
]