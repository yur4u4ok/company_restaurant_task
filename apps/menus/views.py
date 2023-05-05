from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import MenuModel
from .serializers import MenuSerializer

from datetime import datetime


class MenusGet(ListAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)


class MenuRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)


class MenuVoteView(GenericAPIView):
    queryset = MenuModel.objects.all()

    def patch(self, *args, **kwargs):
        menu = self.get_object()

        if (menu.day.year != datetime.now().year) or (menu.day.month != datetime.now().month) \
                or (menu.day.day != datetime.now().day):
            return Response("You can only vote for today's menu", status=status.HTTP_400_BAD_REQUEST)

        menu.votes += 1
        menu.save()
        serializer = MenuSerializer(menu)

        return Response(serializer.data, status.HTTP_200_OK)


class MenuGetCurrentDayMenu(ListAPIView):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    queryset_filter = MenuModel.objects.filter(day__year=year, day__month=month, day__day=day)
    queryset = queryset_filter.order_by("-votes")[0:1]

    serializer_class = MenuSerializer


class MenuGetResultsForTheCurrentDayView(ListAPIView):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    queryset = MenuModel.objects.filter(day__year=year, day__month=month, day__day=day)
    serializer_class = MenuSerializer
