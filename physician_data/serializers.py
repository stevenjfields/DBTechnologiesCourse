from rest_framework import routers, serializers, viewsets
from .models import BeneficiaryData, Payment, Provider, Address
from django_restql.mixins import DynamicFieldsMixin

class ProviderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class AddressSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class BeneficiaryDataSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = BeneficiaryData
        fields = '__all__'

class PaymentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'