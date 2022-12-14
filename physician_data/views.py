from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, mixins, generics
from .models import BeneficiaryData, Payment, Physician, Address
from .serializers import AddressSerializer, BeneficiaryDataSerializer, PaymentSerializer, PhysicianSerializer
from django_filters import rest_framework as filters

# Create your views here.
class PhysicianFilter(filters.FilterSet):
    class Meta:
        model = Physician
        fields = '__all__'
class AddressFilter(filters.FilterSet):
    class Meta:
        model = Address
        fields = '__all__'
class BeneficiaryFilter(filters.FilterSet):
    class Meta:
        model = BeneficiaryData
        fields = '__all__'
class PaymentFilter(filters.FilterSet):
    class Meta:
        model = Payment
        fields = '__all__'

class PhysicianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer
    filterset_class = PhysicianFilter

class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

class BeneficiaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BeneficiaryData.objects.all()
    serializer_class = BeneficiaryDataSerializer
    filterset_class = BeneficiaryFilter

class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter