from rest_framework import viewsets

from food.models import FoodCategory
from food_api.serializers import FoodListSerializer


class FoodListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()
    serializer_class = FoodListSerializer
    # Вью который вернет жсон
    # Только чтение
    http_method_names = ('get',)
