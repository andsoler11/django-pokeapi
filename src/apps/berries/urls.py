from django.urls import path
from .views import display_histogram

urlpatterns = [
    path("", display_histogram, name="display-histogram"),
]