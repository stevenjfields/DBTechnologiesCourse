from django.db import models
from numpy import number

# Create your models here.

class Provider(models.Model):
    ENTITY_CHOICES = [
        ("O", "Organization"),
        ("I", "Individual")
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]

    NPI = models.IntegerField(verbose_name="National Provider Identifier")
    Last_Name = models.CharField(max_length=64)
    First_Name = models.CharField(max_length=64)
    MI = models.CharField(verbose_name="Middle Initial", max_length=8, blank=True)
    Credentials = models.CharField(max_length=128)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Entity_Type = models.CharField(max_length=1, choices=ENTITY_CHOICES)
    Provider_Type = models.CharField(max_length=128)
    MPI = models.CharField(verbose_name="Medicare Participation Indicator", max_length=8)

    def __str__(self):
        return f"{self.Last_Name}, {self.First_Name}"

class Address(models.Model):
    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)
    Street_Address_1 = models.CharField(max_length=256)
    Street_Address_2 = models.CharField(max_length=256, blank=True)
    City = models.CharField(max_length=128)
    State = models.CharField(max_length=2)
    State_FIPS = models.CharField(max_length=4)
    Zip5 = models.CharField(max_length=5)
    RUCA = models.IntegerField()
    RUCA_Desc = models.CharField(max_length=256)
    Country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Street_Address_1}, {self.City}, {self.State}"


class BeneficiaryData(models.Model):
    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)
    Total_Benes = models.IntegerField(blank=True, null=True)
    Drug_Total_Benes = models.IntegerField(blank=True, null=True)
    Med_Total_Benes = models.IntegerField(blank=True, null=True)
    Average_Age = models.IntegerField(blank=True, null=True)
    Age_LT_65_Count = models.IntegerField(blank=True, null=True)
    Age_65_74_Count = models.IntegerField(blank=True, null=True)
    Age_75_84_Count = models.IntegerField(blank=True, null=True)
    Age_GT_84_Count = models.IntegerField(blank=True, null=True)
    Female_Count = models.IntegerField(blank=True, null=True)
    Male_Count = models.IntegerField(blank=True, null=True)
    Race_White_Count = models.IntegerField(blank=True, null=True)
    Race_Black_Count = models.IntegerField(blank=True, null=True)
    Race_API_Count = models.IntegerField(blank=True, null=True)
    Race_Hispanic_Count = models.IntegerField(blank=True, null=True)
    Race_NatInd_Count = models.IntegerField(blank=True, null=True)
    Race_Other_Count = models.IntegerField(blank=True, null=True)
    Dual_Count = models.IntegerField(blank=True, null=True)
    Not_Dual_Count = models.IntegerField(blank=True, null=True)
    AFib_Pct = models.FloatField(blank=True, null=True)
    Alzhmr_Pct = models.FloatField(blank=True, null=True)
    Asthma_Pct = models.FloatField(blank=True, null=True)
    Cancer_Pct = models.FloatField(blank=True, null=True)
    Heart_Failure_Pct = models.FloatField(blank=True, null=True)
    Kidney_Disease_Pct = models.FloatField(blank=True, null=True)
    COPD_Pct = models.FloatField(blank=True, null=True)
    Depression_Pct = models.FloatField(blank=True, null=True)
    Diabetes_Pct = models.FloatField(blank=True, null=True)
    Hyplpdma_Pct = models.FloatField(blank=True, null=True)
    Hyprtnsn_Pct = models.FloatField(blank=True, null=True)
    Ischemic_Heart_Disease_Pct = models.FloatField(blank=True, null=True)
    Osteoporosis_Pct = models.FloatField(blank=True, null=True)
    Rh_Os_Arthritis_Pct = models.FloatField(blank=True, null=True)
    Schizo_Pct = models.FloatField(blank=True, null=True)
    Stroke_Pct = models.FloatField(blank=True, null=True)
    Avg_Risk_Score = models.FloatField(blank=True, null=True)

class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("Total", "Total"),
        ("Drug", "Drug"),
        ("Medical", "Medical")
    ]

    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)
    Type = models.CharField(max_length=16, choices=PAYMENT_CHOICES, null=True)
    Supressed = models.CharField(max_length=2, null=True, blank=True)
    HCPCS_Codes = models.IntegerField(blank=True, null=True)
    Services = models.IntegerField(blank=True, null=True)
    Submitted_Charges = models.FloatField(blank=True, null=True)
    Mdcr_Allowed_Amt = models.FloatField(blank=True, null=True)
    Mdcr_Payment_Amt = models.FloatField(blank=True, null=True)
    Mdcr_Stdzd_Amt = models.FloatField(blank=True, null=True)
