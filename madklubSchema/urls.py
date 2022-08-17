from .views import SchemaView
from django.urls import path

urlpatterns = [
    path('', SchemaView.as_view(), name='schemas')
]