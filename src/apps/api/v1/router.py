from rest_framework import routers

from apps.berries.views import BerriesViewSet

router = routers.DefaultRouter()

router.register(r"", BerriesViewSet, basename="allBerryStats")