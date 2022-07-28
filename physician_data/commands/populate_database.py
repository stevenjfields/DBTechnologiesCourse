from django.core.management.base import BaseCommand, CommandError
from physician_data.models import *

FIELD_GROUPS = {
    "Providers": [
        'Rndrng_NPI',
        'Rndrng_Prvdr_Last_Org_Name',
        'Rndrng_Prvdr_First_Name',
        'Rndrng_Prvdr_MI',
        'Rndrng_Prvdr_Crdntls',
        'Rndrng_Prvdr_Gndr',
        'Rndrng_Prvdr_Ent_Cd',
        'Rndrng_Prvdr_Type',
        'Rndrng_Prvdr_Mdcr_Prtcptg_Ind'
    ],
    "Addresses": [
        'Rndrng_Prvdr_St1',
        'Rndrng_Prvdr_St2',
        'Rndrng_Prvdr_City',
        'Rndrng_Prvdr_State_Abrvtn',
        'Rndrng_Prvdr_State_FIPS',
        'Rndrng_Prvdr_Zip5',
        'Rndrng_Prvdr_RUCA',
        'Rndrng_Prvdr_RUCA_Desc',
        'Rndrng_Prvdr_Cntry',
    ],
    "Payments": [
        'Tot_HCPCS_Cds',
        'Tot_Srvcs',
        'Tot_Sbmtd_Chrg',
        'Tot_Mdcr_Alowd_Amt',
        'Tot_Mdcr_Pymt_Amt',
        'Tot_Mdcr_Stdzd_Amt',
        'Drug_Tot_HCPCS_Cds',
        'Drug_Tot_Srvcs',
        'Drug_Mdcr_Alowd_Amt',
        'Drug_Mdcr_Pymt_Amt',
        'Drug_Mdcr_Stdzd_Amt',
        'Med_Tot_HCPCS_Cds',
        'Med_Tot_Srvcs',
        'Med_Mdcr_Alowd_Amt',
        'Med_Mdcr_Pymt_Amt',
        'Med_Mdcr_Stdzd_Amt'
    ],
    "Beneficiary_Data": [
        'Tot_Benes',
        'Drug_Tot_Benes',
        'Med_Tot_Benes'
        'Bene_Avg_Age',
        'Bene_Age_LT_65_Cnt',
        'Bene_Age_65_74_Cnt',
        'Bene_Age_75_84_Cnt',
        'Bene_Age_GT_84_Cnt',
        'Bene_Feml_Cnt',
        'Bene_Male_Cnt',
        'Bene_Race_Wht_Cnt',
        'Bene_Race_Black_Cnt',
        'Bene_Race_API_Cnt',
        'Bene_Race_Hspnc_Cnt',
        'Bene_Race_NatInd_Cnt',
        'Bene_Race_Othr_Cnt',
        'Bene_Dual_Cnt',
        'Bene_Ndual_Cnt',
        'Bene_CC_AF_Pct',
        'Bene_CC_Alzhmr_Pct',
        'Bene_CC_Asthma_Pct',
        'Bene_CC_Cncr_Pct',
        'Bene_CC_CHF_Pct',
        'Bene_CC_CKD_Pct',
        'Bene_CC_COPD_Pct',
        'Bene_CC_Dprssn_Pct',
        'Bene_CC_Dbts_Pct',
        'Bene_CC_Hyplpdma_Pct',
        'Bene_CC_Hyprtnsn_Pct',
        'Bene_CC_IHD_Pct',
        'Bene_CC_Opo_Pct',
        'Bene_CC_RAOA_Pct',
        'Bene_CC_Sz_Pct',
        'Bene_CC_Strok_Pct',
        'Bene_Avg_Risk_Scre'
    ]
}

class Command(BaseCommand):
    help = 'Imports data from designated flat file into the database.'

    def add_arguments(self, parser) -> None:
        parser.add_argument('file_name', type=str)
        return super().add_arguments(parser)

    def handle(self, *args, **options):

        return super().handle(*args, **options)