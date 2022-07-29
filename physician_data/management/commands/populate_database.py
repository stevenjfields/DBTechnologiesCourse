from django.core.management.base import BaseCommand, CommandError
from physician_data.models import *
import pandas as pd
import numpy as np

class Command(BaseCommand):
    help = 'Imports data from designated flat file into the database.'

    def add_arguments(self, parser) -> None:
        parser.add_argument('file_name', type=str)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        df = pd.DataFrame()
        if options['file_name']:
            try:
                df = pd.read_csv(options['file_name'], encoding='ISO-8859-1')
            except Exception as e:
                print(e)
                return
        else:
            print('No file name provided.')
            return

        df = df.replace({np.nan: None})

        for ind in df.index:
            p = Physician.objects.create(
                NPI = df['Rndrng_NPI'][ind],
                Last_Name_Or_Org = df['Rndrng_Prvdr_Last_Org_Name'][ind],
                First_Name = df['Rndrng_Prvdr_First_Name'][ind],
                MI = df['Rndrng_Prvdr_MI'][ind],
                Credentials = df['Rndrng_Prvdr_Crdntls'][ind],
                Gender = df['Rndrng_Prvdr_Gndr'][ind],
                Entity_Type = df['Rndrng_Prvdr_Ent_Cd'][ind],
                Physician_Type = df['Rndrng_Prvdr_Type'][ind],
                MPI = df['Rndrng_Prvdr_Mdcr_Prtcptg_Ind'][ind]
            )

            Address.objects.create(
                Physician = p,
                Street_Address_1 = df['Rndrng_Prvdr_St1'][ind],
                Street_Address_2 = df['Rndrng_Prvdr_St2'][ind],
                City = df['Rndrng_Prvdr_City'][ind],
                State = df['Rndrng_Prvdr_State_Abrvtn'][ind],
                State_FIPS = df['Rndrng_Prvdr_State_FIPS'][ind],
                Zip5 = df['Rndrng_Prvdr_Zip5'][ind],
                RUCA = df['Rndrng_Prvdr_RUCA'][ind],
                RUCA_Desc = df['Rndrng_Prvdr_RUCA_Desc'][ind],
                Country = df['Rndrng_Prvdr_Cntry'][ind],
            )

            BeneficiaryData.objects.create(
                Physician = p,
                Total_Benes = df['Tot_Benes'][ind],
                Drug_Total_Benes = df['Drug_Tot_Benes'][ind],
                Med_Total_Benes = df['Med_Tot_Benes'][ind],
                Average_Age = df['Bene_Avg_Age'][ind],
                Age_LT_65_Count = df['Bene_Age_LT_65_Cnt'][ind],
                Age_65_74_Count = df['Bene_Age_65_74_Cnt'][ind],
                Age_75_84_Count = df['Bene_Age_75_84_Cnt'][ind],
                Age_GT_84_Count = df['Bene_Age_GT_84_Cnt'][ind],
                Female_Count = df['Bene_Feml_Cnt'][ind],
                Male_Count = df['Bene_Male_Cnt'][ind],
                Race_White_Count = df['Bene_Race_Wht_Cnt'][ind],
                Race_Black_Count = df['Bene_Race_Black_Cnt'][ind],
                Race_API_Count = df['Bene_Race_API_Cnt'][ind],
                Race_Hispanic_Count = df['Bene_Race_Hspnc_Cnt'][ind],
                Race_NatInd_Count = df['Bene_Race_NatInd_Cnt'][ind],
                Race_Other_Count = df['Bene_Race_Othr_Cnt'][ind],
                Dual_Count = df['Bene_Dual_Cnt'][ind],
                Not_Dual_Count = df['Bene_Ndual_Cnt'][ind],
                AFib_Pct = df['Bene_CC_AF_Pct'][ind],
                Alzhmr_Pct = df['Bene_CC_Alzhmr_Pct'][ind],
                Asthma_Pct = df['Bene_CC_Asthma_Pct'][ind],
                Cancer_Pct = df['Bene_CC_Cncr_Pct'][ind],
                Heart_Failure_Pct = df['Bene_CC_CHF_Pct'][ind],
                Kidney_Disease_Pct = df['Bene_CC_CKD_Pct'][ind],
                COPD_Pct = df['Bene_CC_COPD_Pct'][ind],
                Depression_Pct = df['Bene_CC_Dprssn_Pct'][ind],
                Diabetes_Pct = df['Bene_CC_Dbts_Pct'][ind],
                Hyplpdma_Pct = df['Bene_CC_Hyplpdma_Pct'][ind],
                Hyprtnsn_Pct = df['Bene_CC_Hyprtnsn_Pct'][ind],
                Ischemic_Heart_Disease_Pct = df['Bene_CC_IHD_Pct'][ind],
                Osteoporosis_Pct = df['Bene_CC_Opo_Pct'][ind],
                Rh_Os_Arthritis_Pct = df['Bene_CC_RAOA_Pct'][ind],
                Schizo_Pct = df['Bene_CC_Sz_Pct'][ind],
                Stroke_Pct = df['Bene_CC_Strok_Pct'][ind],
                Avg_Risk_Score = df['Bene_Avg_Risk_Scre'][ind]
            )

            Payment.objects.create(
                Physician = p,
                Type = 'Total',
                HCPCS_Codes = df['Tot_HCPCS_Cds'][ind],
                Services = df['Tot_Srvcs'][ind],
                Submitted_Charges = df['Tot_Sbmtd_Chrg'][ind],
                Mdcr_Allowed_Amt = df['Tot_Mdcr_Alowd_Amt'][ind],
                Mdcr_Payment_Amt = df['Tot_Mdcr_Pymt_Amt'][ind],
                Mdcr_Stdzd_Amt = df['Tot_Mdcr_Stdzd_Amt'][ind],
            )

            Payment.objects.create(
                Physician = p,
                Type = 'Drug',
                Supressed = df['Drug_Sprsn_Ind'][ind],
                HCPCS_Codes = df['Drug_Tot_HCPCS_Cds'][ind],
                Services = df['Drug_Tot_Srvcs'][ind],
                Submitted_Charges = df['Drug_Sbmtd_Chrg'][ind],
                Mdcr_Allowed_Amt = df['Drug_Mdcr_Alowd_Amt'][ind],
                Mdcr_Payment_Amt = df['Drug_Mdcr_Pymt_Amt'][ind],
                Mdcr_Stdzd_Amt = df['Drug_Mdcr_Stdzd_Amt'][ind]
            )

            Payment.objects.create(
                Physician = p,
                Type = "Medical",
                Supressed = df['Med_Sprsn_Ind'][ind],
                HCPCS_Codes = df['Med_Tot_HCPCS_Cds'][ind],
                Services = df['Med_Tot_Srvcs'][ind],
                Submitted_Charges = df['Med_Sbmtd_Chrg'][ind],
                Mdcr_Allowed_Amt = df['Med_Mdcr_Alowd_Amt'][ind],
                Mdcr_Payment_Amt = df['Med_Mdcr_Pymt_Amt'][ind],
                Mdcr_Stdzd_Amt = df['Med_Mdcr_Stdzd_Amt'][ind],
            )

            if ind % 100 == 0 and ind != 0:
                print(f"Successfully created {ind} physicians")
            
            if ind % 10000 == 0 and ind != 0:
                return
        return super().handle(*args, **options)