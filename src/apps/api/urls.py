from django.urls import include, path

urlpatterns = [
    path("", include(("apps.api.v1.urls", "apps.api.v1"), namespace="v1")), 
]