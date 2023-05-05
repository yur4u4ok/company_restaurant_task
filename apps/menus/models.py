from django.db import models

from apps.restaurant.models import RestaurantModel


class MenuModel(models.Model):
    class Meta:
        db_table = 'menus'

    day = models.DateTimeField(auto_now=True)
    first_course = models.CharField(max_length=100, blank=True)
    main_course = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100, blank=True)
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE, related_name='menu')
    votes = models.IntegerField(default=0)
