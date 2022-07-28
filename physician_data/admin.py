from django.contrib import admin
from physician_data.models import Provider, Address, BeneficiaryData, Payment

# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass

class BeneficiaryDataAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(BeneficiaryData, BeneficiaryDataAdmin)
admin.site.register(Payment, PaymentAdmin)