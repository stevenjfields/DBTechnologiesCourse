from django.contrib import admin
from physician_data.models import Physician, Address, BeneficiaryData, Payment

# Register your models here.
class PhysicianAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass

class BeneficiaryDataAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(BeneficiaryData, BeneficiaryDataAdmin)
admin.site.register(Payment, PaymentAdmin)