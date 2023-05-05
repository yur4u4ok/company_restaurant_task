from django.urls import path, include

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('menus', include('apps.menus.urls')),
    path('restaurant', include('apps.restaurant.urls')),

]
