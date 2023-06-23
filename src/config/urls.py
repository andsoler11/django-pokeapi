from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('allBerryStats', include('apps.api.urls')),
    path('', include('apps.berries.urls'))
]
