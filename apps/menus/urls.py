from django.urls import path

from .views import MenusGet, MenuRetrieveUpdateDelete, MenuVoteView, MenuGetCurrentDayMenu, \
    MenuGetResultsForTheCurrentDayView

urlpatterns = [
    path('', MenusGet.as_view(), name='get_menus'),
    path('/<int:pk>', MenuRetrieveUpdateDelete.as_view(), name='get_update_delete_menu'),
    path('/<int:pk>/vote', MenuVoteView.as_view(), name='vote_for_menu'),
    path('/current_day_menu', MenuGetCurrentDayMenu.as_view(), name='get_current_day_menu'),
    path('/current_day/results', MenuGetResultsForTheCurrentDayView.as_view(), name='get_current_day_results'),
]
