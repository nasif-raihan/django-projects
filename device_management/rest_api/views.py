from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Company, Employee, Device, Checkout
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    DeviceSerializer,
    CheckoutSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=["get"])
    def devices(self, request, pk=None):
        employee = self.get_object()
        devices = Device.objects.filter(checkout__employee=employee)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=["get"])
    def checkouts(self, request, pk=None):
        device = self.get_object()
        checkouts = Checkout.objects.filter(device=device)
        serializer = CheckoutSerializer(checkouts, many=True)
        return Response(serializer.data)


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
