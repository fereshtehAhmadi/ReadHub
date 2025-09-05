from rest_framework.viewsets import ModelViewSet
from src.apps.user.models import LibraryStaff
from src.apps.user.v1.presentation.admin.setting.serializers import (
    CreateEmployeeSerializer,
    EmployeeDetailSerializer,
    EmployeeListSerializer,
    EmployeeUpdateSerializer,
)


class EmployeeViewSet(ModelViewSet):
    queryset = LibraryStaff.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EmployeeListSerializer
        elif self.action == "retrieve":
            return EmployeeDetailSerializer
        elif self.action == "create":
            return CreateEmployeeSerializer
        elif self.action in ["update", "partial_update"]:
            return EmployeeUpdateSerializer
        return EmployeeDetailSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
