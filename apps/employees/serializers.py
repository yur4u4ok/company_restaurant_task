from apps.employees.models import ProfileModel, EmployeeModel as Employee

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

EmployeeModel: Employee = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age')


class EmployeeSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = EmployeeModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',
            'created_at', 'updated_at', 'profile')

        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser',
                            'created_at', 'updated_at')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        employee = EmployeeModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, employee=employee)

        return employee
