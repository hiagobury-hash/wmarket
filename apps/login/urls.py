from django.urls import path
from apps.login.views import (
    index,
)

urlpatterns = [
    path('', index),
]
