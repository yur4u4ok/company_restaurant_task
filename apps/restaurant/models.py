from django.db import models


class RestaurantModel(models.Model):
    class Meta:
        db_table = 'restaurant'

    restaurant_name = models.CharField(max_length=40)
