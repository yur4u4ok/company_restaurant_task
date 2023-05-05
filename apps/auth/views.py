from apps.employees.serializers import EmployeeSerializer

from rest_framework.generics import CreateAPIView

from rest_framework.permissions import AllowAny


class AuthRegisterView(CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)
