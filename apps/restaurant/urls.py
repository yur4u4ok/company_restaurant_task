from django.urls import path

from .views import RestaurantListCreateMenuView, RestaurantListCreateView

urlpatterns = [
    path('', RestaurantListCreateView.as_view(), name='create_list_restaurants'),
    path('/<int:pk>/menus', RestaurantListCreateMenuView.as_view(), name='list_create_menu'),

]
