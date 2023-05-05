from rest_framework.serializers import ModelSerializer, RelatedField

from core.dataclasses.restaurant_dataclass import Restaurant

from .models import MenuModel


class RestaurantRelatedFieldSerializer(RelatedField):
    def to_representation(self, value: Restaurant):
        return {'id': value.id, 'name': value.restaurant_name}


class MenuSerializer(ModelSerializer):
    restaurant = RestaurantRelatedFieldSerializer(read_only=True)

    class Meta:
        model = MenuModel
        fields = ('id', 'day', 'first_course', 'main_course', 'dessert', 'restaurant', 'votes')
        read_only_fields = ('id', 'day', 'restaurant', 'votes')
