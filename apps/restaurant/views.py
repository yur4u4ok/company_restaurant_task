from apps.restaurant.serializers import RestaurantSerializer

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import RestaurantModel
from apps.menus.serializers import MenuSerializer


class RestaurantListCreateView(ListCreateAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (AllowAny,)


class RestaurantListCreateMenuView(ListCreateAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        restaurant = self.get_object()
        serializer.save(restaurant=restaurant)

    def get(self, *args, **kwargs):
        restaurant = self.get_object()
        serializer = self.serializer_class(restaurant.menu, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
