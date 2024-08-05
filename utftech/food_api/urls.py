from django.urls import include, path
from rest_framework import routers

from food_api.constants import API_VERSION
from food_api.views import FoodListViewSet

router = routers.DefaultRouter()
router.register(r'foods', FoodListViewSet, basename='foods')

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
]
