from rest_framework.serializers import ModelSerializer

from apps.restaurant.models import RestaurantModel

from apps.menus.serializers import MenuSerializer


class RestaurantSerializer(ModelSerializer):
    menu = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = RestaurantModel
        fields = ('id', 'restaurant_name', 'menu')
