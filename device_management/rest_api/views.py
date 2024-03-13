from rest_framework.viewsets import ModelViewSet
from .models import Company, Employee, TakenDeviceHistory
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceView(ModelViewSet):
    queryset = TakenDeviceHistory.objects.all()
    serializer_class = DeviceSerializer
