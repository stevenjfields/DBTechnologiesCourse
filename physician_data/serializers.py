from rest_framework import routers, serializers, viewsets
from .models import BeneficiaryData, Payment, Physician, Address
from django_restql.mixins import DynamicFieldsMixin

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
class PhysicianSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Physician
        fields = ['id', 'NPI', 'Last_Name_Or_Org', 'First_Name', 'MI', 
        'Credentials', 'Gender', 'Entity_Type', 'Physician_Type', 'MPI',
        'address', 'beneficiary_data', 'payments']
